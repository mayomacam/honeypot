import ssht
import argparse
import sys

parser = argparse.ArgumentParser(description='Python3 ssh honeypot')
parser.add_argument(
    'ip',
    metavar='<IP_Address>',
    type=str,
    default='127.0.0.1',
    help='IP on which Honeypot would be running usually localhost')

parser.add_argument(
    'port',
    metavar='<Ports>',
    type=int,
    nargs='+',
    help='IP on which ssh would be running usually port 22')

parser.add_argument(
    'conn',
    metavar='<Log_file>',
    type=str,
    default='connections.log',
    help='The File on which Honeypot would be logging any connections')

parser.add_argument(
    'auth',
    metavar='<Log_file>',
    type=str,
    default='auth.log',
    help='The File on which Honeypot would be logging any auths')

args = parser.parse_args()
print(args)

ip = args.ip
port = args.port
logfile1 = args.conn
logfile2 = args.auth

print(ip, port, logfile1, logfile2)

ssh_run = ssht.sshtp(ip, port, logfile1, logfile2)
ssh_run.run()
