#!/usr/bin/env python

from bottle import route, request, run                                             
import argparse

# parse cli arguments
parser = argparse.ArgumentParser()
parser.add_argument("--host",
                    help="Server address to bind to. Default is localhost (127.0.0.1)")
parser.add_argument("-p", "--port",
                    help="Server port to bind to. Default is 8080",
                    type=int)
args = parser.parse_args()

# set host and port variables
host = args.host if args.host else "localhost"
port = args.port if args.port else 8080

# Define POST route
@route('/', method='POST')                   
def default():
    # print request to console
    print(request.json)                                              

# Start listening on <host>:<port>
run(host=host, port=port)