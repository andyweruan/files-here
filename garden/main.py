import webapp2
import jinja2
import os
import random
import logging
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))



class Flower(ndb.Model): #flower is a kind of model   we get the constructor for free
    top = ndb.IntegerProperty()
    left = ndb.IntegerProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        left = random.randint(0, 100)
        top = random.randint(0, 100)

        new_flower = Flower(top = top, left = left)
#        logging.info(new_flower)
        new_flower.put() #put is creating something new
        #fetch() is getting whole list and get() is only one
        #update also put
        #delete is key.delete
        flowers = Flower.query().fetch() #look for all these stuff and then fetch them all back to me
        template_values = {'flowers': flowers}
#        self.response.write('Hello World!')
        template = jinja_environment.get_template('garden.html')
        self.response.write(template.render(template_values))
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
