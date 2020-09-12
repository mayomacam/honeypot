"""
Simple TCP Honeypot logger:

Usage: honeypot <config_file_path>

"""
from docopt import docopt

args = docopt(__doc__)

print("Config file: %s",args["<config_file_path>"])


