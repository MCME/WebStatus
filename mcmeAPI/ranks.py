from datetime import datetime

from lib import requests, yaml
from db import db_session as ses
from db.models import User


MCME_YAML_URL = 'http://build.mcmiddleearth.com/cache/uploads/users.yml'


def fetch_yaml():
    '''fetches yaml file from mcmiddleearth,
       loads, parses, and returns python object'''
    response = requests.get(MCME_YAML_URL)
    raw_yaml = response.content
    response.close()
    return yaml.load(raw_yaml)


def update_user_db():
    for user, attr in fetch_yaml()['users'].iteritems():
        r = ses.query(User).filter(User.name==user).all()
        if not r: 
            r = User()
        r.rank=attr['group']
        r.name=user
        r.updated = datetime.now()
        ses.add(r)
    ses.commit()
    return

def get_ranks(rank):
    '''accepts string denoting MCME rank
       returns list containing names of desired rank
       or none'''
    user_list = ses.query(User).filter(User.rank==rank).all()
    return [u.name for u in user_list]
    