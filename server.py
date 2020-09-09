import time
import http.server
import logging
import os

HOST = ''
port = 8080
"""
def loger(address, data=''):

    c = time.ctime()
    with open('netowrk.log', 'a') as s:
        p = "time:{} {}:{} , data:{}\n".format(c, address[0], address[1], data)
        s.write(p)
    
"""
def run(
        server_class=http.server.HTTPServer,
        handler_class=http.server.SimpleHTTPRequestHandler,
        port=8080):

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    # httpdkenlogger = logging.getLogger('httpd-ken')
    # #setup file handler
    # fh = logging.FileHandler('connections.log')
    # fh.setLevel(logging.INFO)
    # frmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # fh.setFormatter(frmt)
    # # Add this handler to the logger
    # httpdkenlogger.addHandler(fh)

    # logging.info("Server starting...\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
