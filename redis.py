import redis

cache = redis.Redis()

cache.set('bing', 'baz')

pipe = cache.pipeline()

pipe.set('foo', 'bar')
pipe.get('bing')
# the EXECUTE call sends all buffered commands to the server, returning a list of responses, one for each command.
pipe.execute()
# [True, 'baz']


# redis data structures examples


import redis

cache = redis.Redis()

cache.set("mykey", "myvalue")

print(cache.get("mykey"))
# b'myvalue' // All returning keys and values are "byte" in Python 3, "unicode" in Python 2

# nx and xx

print(cache.get("mykey"))
# b'myvalue'

print(cache.setnx("mykey", "mynewvalue"))
# False

print(cache.get("mykey"))
# b'myvalue'

print(cache.setxx("mykey", "mynewvalue"))
# True

print(cache.get("mykey"))
# b'mynewvalue'

# incr

cache.set("counter", 100)

print(cache.incr("counter"))
# 101 // integer

print(cache.get("counter"))
# b'101' // byte


# Questions

while questions:
    question = questions.pop()
    try:
        answer(question)
    except Exception:
        pass

demo_app()
