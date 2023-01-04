import sys
import requests

def helloworld(out):
    out.write("Hello world of Python\n")

def rest(out):
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    out.write(str(r.status_code))
