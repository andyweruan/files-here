import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))


'''
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
'''
env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('main.html')
        self.response.out.write(template.render())
    def post(self): ## here's the new POST method in the MainHandler
        activity = self.request.get('activity')
        name = self.request.get('noun1')
        teacher = self.request.get('teacher')
        fun = self.request.get('fun')
        show = self.request.get('show')
        template = jinja_environment.get_template('result.html')
        vals = {'activity':activity, 'noun1':name, 'teacher':teacher, 'fun':fun, 'show':show}

        self.response.out.write(template.render(vals))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
