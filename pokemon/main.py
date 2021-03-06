import webapp2
import jinja2
import os
#set up jinja environment.
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('home.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
