from twisted.application import service
from twisted.words.protocols.jabber import jid
from wokkel.client import XMPPClient
from hexbug.protocol import HexBugProtocol

USERNAME = ''
PASSWORD = ''

application = service.Application("hexbug")

jid = jid.internJID(USERNAME)
xmppclient = XMPPClient(jid, PASSWORD)
xmppclient.logTraffic = False

hexbug = HexBugProtocol()
hexbug.setHandlerParent(xmppclient)
xmppclient.setServiceParent(application)
