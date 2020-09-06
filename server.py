import socket
import csv
import time

HOST = ''
PORT = 44444

def logging(address, data=''):
    c = time.ctime()
    with open('netowrk.log','a') as s:
        p = "time:{} {}:{} , data:{}\n".format(c, address[0], address[1], data)
        s.write(p)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try :
            s.bind((HOST,PORT))
            s.listen(100)
        except:
            s.listen(100)
        while True:
            (conn, address) = s.accept()
            with conn:
                conn.settimeout(2)
                print("Got connection from : ", address)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        conn.sendall(b'bye!')
                        conn.close()
                        s.close()
                        main()
                    #conn.sendall(data)
                    #print('Received : ', repr(data))
                    logging(address, data)
                    conn.sendall(b'Bye!')
                    conn.close()
                    s.close()
                    main()

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ('Bye!')
        exit(0)
    except BaseException as e:
        print('Error: {0}'.format(str(e)))
exit(1)