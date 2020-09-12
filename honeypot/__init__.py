class Honeypot:
    def __init__(self, ports):
        for port in ports:
            print("Will be listening on %s" % port)
