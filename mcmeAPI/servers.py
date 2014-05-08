import logging
from datetime import datetime
from lib.minecraft_query import MinecraftQuery
from db.models import Server
from db import db_session as ses
# from google.appengine.api import urlfetch
# from google.appengine.ext import ndb

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

        s = ses.query(Server).get(server)
        if s is None:
            s = Server()
        s.name = server
        s.status = 'online' if not error else 'offline'
        s.players = status.get('players')
        s.num_players = status.get('numplayers')
        s.maxplayers = status.get('maxplayers')
        s.plugins = status.get('plugins')
        s.updated = datetime.now()
        ses.add(s)
    ses.commit()
    return

def get_status(server):
    return ses.query(Server).get(server)  