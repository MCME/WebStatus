from lib import yaml, requests
from mcmeAPI.db import Rank
from google.appengine.api import urlfetch
from google.appengine.ext import ndb

MCME_YAML_URL = 'http://build.mcmiddleearth.com/cache/uploads/users.yml'


def fetch_yaml():
    '''fetches yaml file from mcmiddleearth,
       loads, parses, and returns python object'''
    response = requests.get(MCME_YAML_URL)
    raw_yaml = response.content

    return yaml.load(raw_yaml)

def build_ranks_structure(users):
    '''iterate through parsed_yaml, build dict
       returns: {'rank':[list, of, names]}'''
    ranks = {}
    for user, vals in users.iteritems():
        rank = vals['group']
        if rank == 'root': rank = 'valar'
        if ranks.get(rank): 
            ranks[rank].append(user)
        else:
            ranks[rank] = [user]
    return ranks

def update_rank_db():
    parsed_yaml = fetch_yaml()
    ranks = build_ranks_structure(parsed_yaml['users'])

    for rank, people in ranks.iteritems():
        key = ndb.Key(Rank, rank)
        r = key.get()
        if r is None: 
            r = Rank(id=rank)
        r.rank=rank
        r.members=people
        r.num_members=len(people)
        r.put()

def get_ranks(rank):
    '''accepts string denoting MCME rank
       returns list containing names of desired rank
       or none'''
    key = ndb.Key(Rank, rank)
    return key.get()
