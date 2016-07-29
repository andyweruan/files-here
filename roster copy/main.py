import webapp2
import jinja2
import os
import logging
from google.appengine.ext import ndb

#agpkZXZ-cm9zdGVychQLEgdTdHVkZW50GICAgICAgIAJDA

#URL safekey cheatsheet

# e  This is an entity
# Entity => URL safe key
#urlsafe_key = e.key.urlsafe()
#
#URL Safe String => Entity
#urlsafe_key  #This is a String
#key = ndb.Key(urlsafe=urlsafe_key)
# e = key.get()


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class Student(ndb.Model):
    name = ndb.StringProperty()
    university = ndb.StringProperty()
    team = ndb.StringProperty() #team is 'r' 'b' or 'y'

    def url(self):
        url = '/student?key=' + self.key.urlsafe()
        return url

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Get request

        #NOTHING

        #2 LOGIC   talk to datebase
        students = Student.query().order(Student.name).order(Student.team).fetch()

        #3 Render my resonse
        template_values = {'students': students}
        template = jinja_environment.get_template('list.html')
        self.response.write(template.render(template_values))

    def post(self):
        name = self.request.get('name')
        university = self.request.get('university')
        team = self.request.get('team_color')
        new_student = Student(name = name, university = university, team = team)
        new_student.put()

        self.redirect('/')

class StudentHandler(webapp2.RequestHandler):
    #in your handler, print out student name
    # render a template showing info
    # put info into form so you can update
    def get(self):
        key = self.request.get('key')
        student = ndb.Key(urlsafe=key).get()
        name = student.name
        university = student.university
        team = student.team
        template_values = {'student': student}
        template = jinja_environment.get_template('info.html')
        self.response.write(template.render(template_values))
    def post(self):
        key = self.request.get('key')
        student = ndb.Key(urlsafe=key).get()
        student.name = self.request.get('name')
        student.university = self.request.get('university')
        student.team = self.request.get('team')
        student.put()
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/student', StudentHandler)
], debug=True)
