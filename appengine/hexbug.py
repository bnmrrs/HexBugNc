import os
import cgi
from google.appengine.api import xmpp
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

HEXBUG_XMPP_ADDR = ''

class MainPage(webapp.RequestHandler):
  def get(self):
    hexbug_avaliable = False

    if xmpp.get_presence(HEXBUG_XMPP_ADDR):
      hexbug_avaliable = True

    template_values = {
        'hexbug_avaliable': hexbug_avaliable
        }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

class SendCommand(webapp.RequestHandler):
  def post(self):
    cmd = cgi.escape(self.request.get('command'))
    message_success = False
    self.response.headers['Content-Type'] = 'text/plain'

    if xmpp.get_presence(HEXBUG_XMPP_ADDR):
      status_code = xmpp.send_message(HEXBUG_XMPP_ADDR, cmd)
      message_success = (status_code != xmpp.NO_ERROR)

    if message_success:
      self.response.out.write('Command successfully sent!')
    else:
      self.response.out.write('Unable to send command')


application = webapp.WSGIApplication(
                                      [('/', MainPage),
                                       ('/send_command', SendCommand)],
                                      debug=True)

if __name__ == "__main__":
  run_wsgi_app(application)
