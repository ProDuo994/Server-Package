import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!disconnect"
SERVER = "192.168.68.1"
ADDR = (SERVER, PORT)

class client:
  log = {}
  def _init_(self, ip, status):
    self.ip = ip
    self.status = status

  def remove():
    pass

  def send(addr, format, port, msg):
    log.append("Sent " + msg + " to " + ip)

  def getHistory()
    pass

def onConnect():
  pass

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
currentClient = client(socket.gethostname(), "online")
