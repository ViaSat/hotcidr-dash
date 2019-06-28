from hotcidrdash import app

import argparse
import logging


# Handle CLI options first
parser = argparse.ArgumentParser(description='Web interface for automation of hotcidr')
parser.add_argument('-d', '--debug', help='print debug output')
args = parser.parse_args()

# Pre-flight checks


# Some basic config  TODO: put this into an external file
app.config['LDAP_SEARCH'] = ''
app.config['LDAP_BASE'] = ''
app.config['LDAP_SERVER'] = ''
app.config['LDAP_USER'] = ''
app.config['LDAP_PASS'] = ''

# Logging setup
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler('hotcidrdash.log')
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

app.run(args.debug)
