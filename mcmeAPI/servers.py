from lib.minecraft_query import MinecraftQuery
from mcmeAPI.db import Server
from google.appengine.api import urlfetch
from google.appengine.ext import ndb

SERVERS = ['build', 'freebuild']


def fetch_server_status(server):
    '''return MinecraftQuery full status'''
    query = MinecraftQuery(server+'.mcmiddleearth.com', 25570)
    try:
        status = query.get_rules()
    except:
        status = {'error':'having trouble connecting to the '+server+' server.'}
    return status

def update_server_db():
    '''function run by cron to update the db'''
    for server in SERVERS:
        status = fetch_server_status(server)
        error = status.get('error')

        key = ndb.Key(Server, server)
        s = key.get()
        if s is None:
            s = Server(id=server)
        s.name = server
        s.status = 'online' if not error else 'offline'
        s.players = status.get('players')
        s.num_players = status.get('numplayers')
        s.put()

def get_status(server):
    key = ndb.Key(Server, server)
    return key.get()