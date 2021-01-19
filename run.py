import honeypot
import argparse
from ssh import ssht

parser = argparse.ArgumentParser(description="Python3 honeypot")
parser.add_argument(
    "ip",
    metavar="<IP_Address>",
    type=str,
    default="127.0.0.1",
    help="IP on which Honeypot would be running usually localhost",
)

parser.add_argument("sshport", metavar="<Ports>", type=int, help="Ports On which ssh honepot would be running.")

parser.add_argument("ports", metavar="<Ports>", type=int, nargs="+", help="Ports On which honepot would be running.")

parser.add_argument(
    "log",
    metavar="<Log_file>",
    type=str,
    default="connections.log",
    help="The File on which Honeypot would be logging any connections",
)

args = parser.parse_args()

ip = args.ip
logfile = args.log
sshport = [args.sshport]
port = args.ports

print(ip, logfile, port)
hon = honeypot.honey(ip, port, logfile)
ssh_run = ssht.sshtp(ip, sshport, logfile, logfile)

hon.run()
ssh_run.run()
