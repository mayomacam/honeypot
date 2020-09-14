#!/usr/bin/python3 
import socket
import paramiko
import time
import threading
try:
    import interactive
except ImportError:
    from . import interactive

HOST = ''
PORT = 2222
paramiko.util.log_to_file("demo_server.log")
host_key = paramiko.RSAKey.from_private_key_file('mayomacam', password='qwerty')
def logging(address, data=''):
    c = time.ctime()
    with open('connection.log','a') as s:
        p = "time:{} {}:{} , data:{}\n".format(c, address[0], address[1], data)
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
            logfile_handle = open('auth.txt',"a")
            print("New login: " + username + ":" + password)
            logfile_handle.write(username + ":" + password + "\n")
            logfile_handle.close()
            if (username == "test") and (password == "qwerty"): #need to add a password mech.
                return paramiko.AUTH_SUCCESSFUL
        except:
            return paramiko.AUTH_FAILED
    
    def get_allowed_auths(self, username):
        return "password"

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
    if not channel is None:
        channel.close()
    print("Authenticated!")
    #testing.event.wait(10)
    #if not testing.event.is_set():
        #print("*** Client never asked for a shell.")
        #sys.exit(1)
    chan = transport.open_session()
    chan.get_pty()
    chan.invoke_shell()
    print("*** Here we go!\n")
    interactive.interactive_shell(chan)
    chan.close()
    transport.close()

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        paramiko.util.log_to_file ('conn.log')
        try:
            try :
                s.bind((HOST,PORT))
                s.listen(100)
            except:
                s.listen(100)
            print("Listening for connection ...")
            client, addr = s.accept()
            connection(client,)
            data = client.recv(1024)
            print("Got a connection!")
            logging(addr, data)
        except Exception as e:
            print(str(e))

server()
