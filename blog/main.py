import webapp2
import jinja2
import os
import logging
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class Post(ndb.Model):
    text = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    title = ndb.StringProperty()
    def url(self):
        return '/post?key=' + self.key.urlsafe()

class Comment(ndb.Model):
    text = ndb.StringProperty()
    name = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    post_key = ndb.KeyProperty(kind = Post)

class PostHandler(webapp2.RequestHandler):
    def get(self):
        # get info
        urlsafe_key = self.request.get('key')
        #logic
        key = ndb.Key(urlsafe = urlsafe_key)
        post = key.get()
        comments = Comment.query(Comment.post_key == post.key).order(Comment.date).fetch()
        # render
        template_values = {'post': post, 'comments': comments}
        template = jinja_environment.get_template('post.html')
        self.response.write(template.render(template_values))

    def post(self):
        comment = self.request.get('comment')
        post_key_urlsafe = self.request.get('key')

        post_key = ndb.Key(urlsafe=post_key_urlsafe)
        post = post_key.get()

        comment = Comment(text=comment, name='Anonymous Coward', post_key=post.key)
        comment.put()

        self.redirect(post.url())
class MainHandler(webapp2.RequestHandler):
    def get(self):

        posts = Post.query().fetch()
        template_values = {'posts': posts}
        template = jinja_environment.get_template('home.html')
        self.response.write(template.render(template_values))

    def post(self):
        #get info from request
        title = self.request.get('title')
        text = self.request.get('text')


        #2 Logic interact with database
        post = Post(title = title, text = text)
        post.put()

        #3 render response
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/post', PostHandler)
], debug=True)
