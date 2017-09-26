# encoding=utf-8
"""
  mongodb
"""

import config
from pymongo import MongoClient

cfg = config.project_config

if cfg.get('remote', None):
    print 'select remote mongo'
    _client = MongoClient(host=cfg['mongo']['host'], port=cfg['mongo']['port'])
    conn = _client[cfg['mongo']['db']]

    conn.authenticate(cfg['mongo']['username'], password=cfg['mongo']['password'])

else:
    print 'select local mongo'
    client = MongoClient('localhost', 27017)
    conn = client.get_database(cfg['mongo']['db'])





