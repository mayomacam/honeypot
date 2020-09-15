import honeypot

ip = "127.0.0.1"
port = [8080, 8888, 2222]
logfile = "connections.log"

hon = honeypot.honey(ip, port, logfile)
hon.run()