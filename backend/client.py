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

  def delete():
    del client

  def send(addr, format, port, msg):
    message = ("Sent " + msg + " to " + ip)
    messageId = 1
    log.insert(messageId, message)

  def getHistory()
    print(log)

def onConnect():
  pass

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
currentClient = client(socket.gethostname(), "online")
