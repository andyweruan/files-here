import webapp2
import jinja2
import os
import logging
from google.appengine.ext import ndb
from google.appengine.api import users

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

#Step 1: Write a model for message
#Form to post new message
#Save messages when posted
#Show all the messages
#Add a time stamp and order messages

class Message(ndb.Model):
    text = ndb.StringProperty()
    email = ndb.StringProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):

        messages = Message().query().fetch()
        template_values = {'messages': messages}
        template = jinja_environment.get_template('messageboard.html')
        self.response.write(template.render(template_values))

    def post(self):
        text = self.request.get('text')
        email = users.get_current_user().email()
        new_message = Message(text = text, email = email)
        new_message.put()
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
