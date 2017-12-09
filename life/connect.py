"""
Usage: 
    connect.py <password>

Options:
    -h --help   show this screen
"""
import os
import json
from docopt import docopt



def connect(password):
    name="Real"
    username=json.load(open('username.json'))['username']
    if not username.endswith('@ctc'):
        username+='@ctc'
    cmd_str="rasdial %s %s %s" %(name,username,password)
    os.system(cmd_str)

if __name__== "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    arguments=docopt(__doc__,version="RealSky 0.1")
    password=arguments['<password>']
    connect(password)