import logging
import threading
from socket import socket , timeout

class honey(object):
    def __init__(self, bind_ip, port, logfile):
        if len(port) < 1:
            raise Exception("No ports provided")

        self.ip = bind_ip
        self.ports = port
        self.logfile = logfile
        self.logger = self.prepare_logger()
        self.listener_threads = {}
        self.logger.info(
            "Honeypot running on Ports %s \n logfile is %s",
            self.ports,
            self.logfile)

    def prepare_logger(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%s',
                            filename=self.logfile,
                            filemode='a')
        logger = logging.getLogger(__name__)

        # Adding console handler 
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)
        return logger

    def run(self):
        for port in self.ports:
            self.new_listener_thread(port)

    # def start_listening(self):
    #     for port in self.ports:
    #         self.listener_threads[port] = threading.Thread(
    #             target=self.new_listener_thread(), args=(port))
    #         self.listener_threads[port].start()

    def new_listener_thread(self, port):
        listener = socket()
        listener.bind((self.ip, int(port)))
        listener.listen(5)
        while True:
            client, addr = listener.accept()
            client_handler = threading.Thread(
                target=self.handle_connection, args=(
                    client, port, addr[0], addr[1]))
            client_handler.start()

    def handle_connection(self, client_socket, port, ip, remote_port):
        self.logger.info(f"Connection Recieved : {port},{ip}, {remote_port}")

        client_socket.settimeout(4)
        try:
            data = client_socket.recv(64)
            self.logger.info(
                f"Data recieved : {port}, {ip}, {remote_port}, {data}")
            client_socket.send(
                "Invalid Connection . Access Denied. \n".encode('utf8'))

        except timeout:
            pass

        client_socket.close()
