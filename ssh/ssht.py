import socket
from binascii import hexlify
import threading
import time
from threading import Thread
import _thread
import sys

try:
    import interactive
except ImportError:
    from . import interactive
import paramiko
from paramiko.py3compat import b, u, decodebytes

try:
    paramiko.util.log_to_file("ip.log")
except BaseException:
    a = open("ip.log", "x")
    paramiko.util.log_to_file("ip.log")


class Server(paramiko.ServerInterface):
    def __init__(self, auth):
        self.event = threading.Event()
        self.auth = auth

    """def get_banner():
        return ("SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2", "en-US")"""

    def check_channel_request(self, kind, chanid):
        print("Channel requested: kind={}".format(kind))
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        try:
            logfile_handle = open(self.auth, "a")
            print("New login: " + username + ":" + password)
            logfile_handle.write(username + ":" + password + "\n")
            logfile_handle.close()
            # need to add a password mech.
            if (username == "test") and (password == "~!@#$%^&*()qwertYUIOP"):
                return paramiko.AUTH_SUCCESSFUL
        except BaseException:
            return paramiko.AUTH_FAILED

    def check_auth_publickey(self, username, key):
        user_key = paramiko.RSAKey.from_private_key_file("keys", password="~!@#$%^&*()")
        # user_key2 = paramiko.RSAKey.get_base64(user_key)     #public key
        # print("Key-based authentication: user={}\n key={}".format(username, key))
        if (username == "test") and (key == user_key):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return "password, publickey"
        # return "publickey, password"

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return True


class sshtp(object):
    def __init__(self, ip, ports, conn, auth):
        if len(ports) < 1:
            raise Exception("No ports provided.")

        self.ip = ip
        self.ports = ports
        self.conn = conn
        self.auth = auth
        self.listener_threads = {}
        self.event = threading.Event()

    def connection(self, client):
        print("*" * 120)
        host_key = paramiko.RSAKey.from_private_key_file("ssh/keys", password="~!@#$%^&*()")
        transport = paramiko.Transport(client)
        # transport.local_version = "OpenSSH_8.4p1 Debian-3"           #
        # "SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2"
        transport.local_version = "SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2"
        # transport.load_server_moduli()
        transport.add_server_key(host_key)
        server = Server(self.auth)
        transport.start_server(server=server)
        channel = transport.accept(200)
        if channel is None:
            sys.exit(1)
        print("Authenticated!")

    def main_server_ssh(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                try:
                    s.bind((self.ip, self.ports[0]))
                    s.listen(100)
                except BaseException:
                    s.listen(100)
                print(f"Listening for ssh connection on port {self.ports}...")
                while True:
                    client, address = s.accept()
                    # self.connection(client,address)
                    # threading.Thread(target=self.connection, args=(client, address))
                    _thread.start_new_thread(self.connection, (client,))
                    self.connect(address)
                s.close()
            except Exception as e:
                print(str(e))

    def run(self):
        self.main_server_ssh()

    def connect(self, address):
        c = time.ctime()
        with open(self.conn, "a") as s:
            p = "time:{} {}:{}\n".format(c, address[0], address[1])
            s.write(p)
