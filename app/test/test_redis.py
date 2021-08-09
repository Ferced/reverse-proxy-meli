import redis
import json

def test_redis():
    redis_client = redis.Redis(host = 'localhost',port=6379,db=0)

    redis_client.set("/sites/",""))

    input()
    print(redis_client.get("/sites/"))