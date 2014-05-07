from sqlalchemy import Column, String, Integer, DateTime, PickleType, Boolean
from mcmeAPI.db import Base

class User(Base):
    __tablename__ = 'users'

    name = Column(String(20), primary_key=True)
    group = Column(String(15)) #rank
    updated = Column(DateTime())
    ob = Column(Boolean)
    staff = Column(Boolean)
    permissions = Column(PickleType)
    worlds = Column(PickleType)

    @property
    def serialize(self):
        return {'group':self.group, 
                'name':self.name, 
                'ob':self.ob,
                'staff':self.staff,
                'permissions':self.permissions,
                'worlds':self.worlds,
                'updated':dump_datetime(self.updated) 
                }

    def __repr__(self):
        return '<User %r>' % (self.name)

class Server(Base):
    __tablename__ = 'servers'

    name = Column(String(15), primary_key=True)
    status = Column(String(10))
    players = Column(PickleType)
    maxplayers = Column(Integer)
    num_players = Column(Integer)
    plugins = Column(PickleType)
    updated = Column(DateTime())

    @property
    def serialize(self):
        return ({'name': self.name, 
                 'status': self.status, 
                 'players':self.players, 
                 'num_players':self.num_players, 
                 'maxplayers':self.maxplayers,
                 'plugins':self.plugins
                 'updated':dump_datetime(self.updated)})

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%dT%H:%M:%S")