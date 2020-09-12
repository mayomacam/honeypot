"""
Simple TCP Honeypot logger:

Usage: honeypot <config_file_path>

"""
import configparser
from honeypot import Honeypot
config_filepath = "honeypot.ini"
config = configparser.ConfigParser()
config.read(config_filepath)

ports = config.get(
    "default",
    'ports',
    raw=True,
    fallback="22,80,443,8080,8888,9001")
logfile = config.get(
    "default",
    "logfile",
    raw=True,
    fallback="/var/log/honeypot.log")

print("Ports: %s" % ports)
print("Logfile: %s" % logfile)

ports_list = ports.split(',')

honey = Honeypot(ports_list, logfile)
