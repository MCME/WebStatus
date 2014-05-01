from google.appengine.ext import ndb


class Rank(ndb.Model):
    rank = ndb.StringProperty()
    members = ndb.JsonProperty()