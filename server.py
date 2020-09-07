import time
import http.server

HOST = ''
port = 8080

class myHandler(baseHTTPRequestHandler):

def logging(address, data=''):

    c = time.ctime()
    with open('netowrk.log', 'a') as s:
        p = "time:{} {}:{} , data:{}\n".format(c, address[0], address[1], data)
        s.write(p)


def run(
        server_class=http.server.HTTPServer,
        handler_class=http.server.BaseHTTPRequestHandler,
        port=8080):

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
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
