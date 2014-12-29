#!/usr/bin/python

# https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS5615

import json
import requests
import getopt
import sys
import subprocess
from subprocess import Popen, PIPE

def usage():
    print "Use netquery.py --as <AS-number> --ip <IP-address>"

def get_prefixes_from_as(asnumber):
    url = 'https://stat.ripe.net/data/announced-prefixes/data.json'

    r = requests.get(url + "?resource=AS" + asnumber)
    t = r.text
    j = json.loads(t)

    for i, val in enumerate(j[u'data'][u'prefixes']):
        print val[u'prefix']

def get_as_from_ip(ipnumber):
    s = Popen('whois -h whois.cymru.com " -v ' + ipnumber + '"', shell=True, stdout=PIPE).stdout.read()
    print s

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:i:", ["help", "as=", "ip="])
    except getopt.GetoptError as err:
        print str(err) # will print something like "option -a not recognized"
        # usage()
        sys.exit(2)

    asnumber = ""
    ipnumber = ""
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
            verbose = True
        elif o in ("-a", "--as"):
            asnumber = a
        elif o in ("-i", "--ip"):
            ipnumber = a
        else:
            assert False, "unhandled option"
            usage()

    if asnumber <> "":
        get_prefixes_from_as(asnumber)

    if ipnumber <> "":
        get_as_from_ip(ipnumber)

### MAIN ###
if __name__ == "__main__":
    main()

