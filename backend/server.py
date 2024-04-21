import http
import socketserver   
from http import HTTPStatus
from http import HTTPMethod

class server {
  def _init_(self, ip, port):
    self.ip = ip
    self.port = port
  unreadPackets = []
}
server = server(0.0.0.0, 1)


def send(ip, data):
  pass

def receve():
  if server.unreadPackets > 0:
    pass

while True:
  receve()
