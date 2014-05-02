import os, webapp2, json, jinja2
from google.appengine.api import memcache

#jinja2 initialization
template_dir = os.path.join(os.path.dirname(os.path.dirname((__file__))), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def writeJSON(self, obj):
        self.response.out.write(json.dumps(obj))

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))