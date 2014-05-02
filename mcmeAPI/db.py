from google.appengine.ext import ndb


class Rank(ndb.Model):
    rank = ndb.StringProperty()
    members = ndb.JsonProperty()
    num_members = ndb.IntegerProperty()
    updated = ndb.DateTimeProperty(auto_now=True)

    @property
    def serialize(self):
        return {'rank':self.rank, 'members':self.members, 'num_members':self.num_members, 'updated':dump_datetime(self.updated) }

class Server(ndb.Model):
    name = ndb.StringProperty()
    status = ndb.StringProperty()
    players = ndb.JsonProperty()
    num_players = ndb.IntegerProperty()
    updated = ndb.DateTimeProperty(auto_now=True)

    @property
    def serialize(self):
        return ({'name': self.name, 
                 'status': self.status, 
                 'players':self.players, 
                 'num_players':self.num_players, 
                 'updated':dump_datetime(self.updated)})

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%dT%H:%M:%S")