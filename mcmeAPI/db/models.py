from sqlalchemy import Column, String, Integer, DateTime
from mcmeAPI.db import Base

class User(Base):
    __tablename__ = 'users'

    name = Column(String, primary_key=True)
    rank = Column(String)
    updated = Column(DateTime())

    @property
    def serialize(self):
        return {'rank':self.rank, 'name':self.name, 'updated':dump_datetime(self.updated) }

    def __repr__(self):
        return '<User %r>' % (self.name)

# class Server(ndb.Model):
#     name = ndb.StringProperty()
#     status = ndb.StringProperty()
#     players = ndb.JsonProperty()
#     num_players = ndb.IntegerProperty()
#     updated = ndb.DateTimeProperty(auto_now=True)

#     @property
#     def serialize(self):
#         return ({'name': self.name, 
#                  'status': self.status, 
#                  'players':self.players, 
#                  'num_players':self.num_players, 
#                  'updated':dump_datetime(self.updated)})

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%dT%H:%M:%S")