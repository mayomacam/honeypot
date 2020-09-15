import honeypot
import argparse
import sys

parser = argparse.ArgumentParser(description='Python3 honeypot')
parser.add_argument(
    'ip',
    metavar='<IP_Address>',
    type=str,
    default='127.0.0.1',
    help='IP on which Honeypot would be running usually localhost')

parser.add_argument(
    'log',
    metavar='<Log_file>',
    type=str,
    default='connections.log',
    help='The File on which Honeypot would be logging any connections')

parser.add_argument(
    'ports',
    metavar='<Ports>',
    type=int,
    nargs='+',
    help='IP on which Honeypot would be running usually localhost')

args = parser.parse_args()
print(args)

ip = args.ip
logfile = args.log
port = args.ports

print(ip, logfile, port)
hon = honeypot.honey(ip, port, logfile)
hon.run()
