import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

with open('persons.json') as p:
    data = json.load(p)

with r.pipeline() as pipe:
    for id, person in enumerate(data , start=1):
        pipe.hsetnx('persons', id, str(person))
    pipe.execute()