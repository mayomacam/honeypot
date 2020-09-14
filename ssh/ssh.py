#!/usr/bin/python3 
import socket
import paramiko
import time
import threading
import sys
from threading import Thread
import _thread
try:
    import interactive
except ImportError:
    from . import interactive

HOST = ''
PORT = 2222
paramiko.util.log_to_file("/home/mayomacam/log/demo_server.log")
host_key = paramiko.RSAKey.from_private_key_file('keys', password='~!@#$%^&*()')
def logging(address):
    c = time.ctime()
    with open('/home/mayomacam/log/connection.log','a') as s:
        p = "time:{} {}:{}\n".format(c, address[0], address[1])
        s.write(p)


class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        try:
            logfile_handle = open('/home/mayomacam/log/auth2.log',"a")
            print("New login: " + username + ":" + password)
            logfile_handle.write(username + ":" + password + "\n")
            logfile_handle.close()
            if (username == "test") and (password == "~!@#$%^&*()qwertYUIOP"): #need to add a password mech.
                return paramiko.AUTH_SUCCESSFUL
        except:
            return paramiko.AUTH_FAILED
    
    def get_allowed_auths(self, username):
        return "password, publickey"

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_pty_request(
        self, channel, term, width, height, pixelwidth, pixelheight, modes
    ):
        return True

#class paramiko.server.InteractiveQuery(name='', instructions='', *prompts)



def connection(client):
    transport = paramiko.Transport(client)
    transport.add_server_key(host_key)
    testing = Server()
    transport.start_server(server=testing)

    channel = transport.accept(20)
    print("Authenticated!")
    if not channel is None:
        channel.close()
    #print("Authenticated!")
    #testing.event.wait(10)
    #if not testing.event.is_set():
        #print("*** Client never asked for a shell.")
        #sys.exit(1)
    #transport.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #paramiko.util.log_to_file ('conn.log')
    try:
        try :
             s.bind((HOST,PORT))
             s.listen(100)
        except:
             s.listen(100)
        print("Listening for connection ...")
        while True:
            client, addr = s.accept()
            logging(addr)
            _thread.start_new_thread(connection,(client,))
        s.close()
            #server()
    except Exception as e:
        print(str(e))
            #server()
