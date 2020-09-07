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
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        if self.path == '/up':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Going up')
        elif os.path.isdir(self.path):
            try:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(str(os.listdir(self.path)).encode())
            except Exception:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'error')
        else:
            try:
                with open(self.path, 'rb') as f:
                    data = f.read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(data)
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'not found')
            except PermissionError:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b'no permission')
            except Exception:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'error')
def run(
        server_class=http.server.HTTPServer,
        handler_class=MyHandler,
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
