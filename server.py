from wsgiref.validate import validator
from wsgiref.simple_server import make_server
from app import application

httpd = make_server('', 8001, validator(application))
print("Listening on port 8001....")
httpd.serve_forever()
