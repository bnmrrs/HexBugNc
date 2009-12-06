from twisted.words.xish import domish
from wokkel.xmppim import MessageProtocol, AvailablePresence
from interface import HexBug

class HexBugProtocol(MessageProtocol):
  def connectionMade(self):
    print "Connected!"

    self.hexbug = HexBug()
    self.send(AvailablePresence())

  def connectionLost(self, reason):
    print "Disconnected!"
    print reason

  def onMessage(self, msg):
    if msg["type"] == 'chat' and hasattr(msg, "body"):
      if str(msg.body) == 'forward':
        self.hexbug.walkForward()
        self.respondToCommand(msg, 'Walking Forward')

      elif str(msg.body) == 'reverse':
        self.hexbug.walkReverse()
        self.respondToCommand(msg, 'Reversing')

      elif str(msg.body) == 'right':
        self.hexbug.spinRight()
        self.respondToCommand(msg, 'Spinning Right')

      elif str(msg.body) == 'left':
        self.hexbug.spinLeft()
        self.respondToCommand(msg, 'Spinning Left')

      elif str(msg.body) == 'stop_walk':
        self.hexbug.stopWalk()
        self.respondToCommand(msg, 'Stopping Walk')

      elif str(msg.body) == 'stop_spin':
        self.hexbug.stopSpin()
        self.respondToCommand(msg, 'Stopping Spin')

      elif str(msg.body) == 'kill_all':
        self.hexbug.stopAll()
        self.respondToCommand(msg, 'Stopping All Movement')

      else:
        self.respondToCommand(msg, 'Unknown Command: %s' % msg.body)

  def respondToCommand(self, msg, response):
    print response
    reply = domish.Element((None, "message"))
    reply["to"] = msg["from"]
    reply["from"] = msg["to"]
    reply["type"] = 'chat'
    reply.addElement("body", content=response)

    self.send(reply)

