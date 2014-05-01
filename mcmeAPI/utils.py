import webapp2, json
from google.appengine.api import memcache



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def writeJSON(self, obj):
        self.response.out.write(json.dumps(obj))