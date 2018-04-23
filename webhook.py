#!/usr/bin/python
# coding:utf-8
import urllib
import urllib.parse
import json
from http.server import HTTPServer,BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        length = self.headers.get('content-length')
        data = self.rfile.read(int(length))
        data = json.loads(data.decode('utf-8'))
        branch = print("branch is:", data["project"]["default_branch"])
        project = print("project name is:", data["project"]["name"])
        print(branch, project)

if __name__=="__main__":
    addr = ('',8000)
    server = HTTPServer(addr,RequestHandler)
    server.serve_forever()
