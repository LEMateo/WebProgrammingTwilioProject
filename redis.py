import fakeredis

r= redis.Redis()

r.set('foo',5)
r.set('bar',15)

print(r.get('foo'))

print(r.keys())

print(r.keys('foo'))