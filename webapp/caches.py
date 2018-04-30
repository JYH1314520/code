from django.conf import settings
from django.core.cache import cache
import json

def read_from_cache(keyname):
    key = keyname
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return data

def write_to_cache(keyname,cachevalue):
    key = keyname
    cache.set(key, json.dumps(cachevalue), settings.NEVER_REDIS_TIMEOUT)