import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))


class Email(object):
    global isSpam
    def __init__(self, subject, unread):
        self.subject = subject
        self.unread = unread
        self.isSpam = False

    def SpamToggle(self):
        self.isSpam = True


class ListHandler(webapp2.RequestHandler):
    def get(self):
        emails = [Email("hello", True),
        Email("Welcome to CSSI", False),
        Email("send money now", True),
        ]
        template = jinja_environment.get_template('list.html')
        vals = {'emails': emails}
        for email in emails:
            if 'money' in email.subject:
                email.SpamToggle()
        self.response.write(template.render(vals))

class SingleHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('home.html')
        self.response.write(template.render())

class EmailHandler(webapp2.RequestHandler):
    def get(self):
        #get info out of request
        subject = self.request.get('subject')
        #render our response
        template = jinja_environment.get_template('email.html')
        # vals is the dictionary of values
        self.response.write(template.render({'subject':subject}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/list', ListHandler),
    ('/email', EmailHandler)
], debug=True)
