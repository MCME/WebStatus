from datetime import datetime
import logging
from lib import requests, yaml
from db import db_session as ses
from db.models import User
from sqlalchemy.orm.exc import NoResultFound

MCME_YAML_URL = 'http://build.mcmiddleearth.com/cache/uploads/users.yml'
STAFF = ['valar', 'artisan', 'foreman', 'steward', 'bounder', 'root']

def fetch_yaml():
    '''fetches yaml file from mcmiddleearth,
       loads, parses, and returns python object'''
    response = requests.get(MCME_YAML_URL)
    raw_yaml = response.content
    response.close()
    return yaml.load(raw_yaml)


def update_user_db():
    for user_name, attr in fetch_yaml()['users'].iteritems():
        r = ses.query(User).get(user_name)
        if r is None:
            #logging.warning(user_name+ "not found. Creaing record.")
            r = User()
        group = attr['group']
        r.group = group if group != 'root' else 'valar'
        r.name = user_name
        r.ob = False if group != 'oathbreaker' else True
        r.staff = True if group in STAFF else False
        r.updated = datetime.now()
        r.permissions = attr.get('permissions')
        r.worlds = attr.get('worlds')
        ses.add(r)
    ses.commit()
    return

def get_user(user_name):
    '''user_name is string denoting user name
       returns user object or None'''
    return ses.query(User).get(user_name)

def get_user_group(group):
    '''accepts string denoting MCME group
       returns list containing names of desired group
       or empty list'''
    if group == 'staff':
        user_list = ses.query(User).filter(User.staff==True).all()
    else:
        user_list = ses.query(User).filter(User.group==group).all()
    return [u.name for u in user_list]
    