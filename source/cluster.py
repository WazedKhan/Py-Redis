from redis.cluster import RedisCluster

rc = RedisCluster(host='localhost', port=16379)

print(rc.get_nodes())
# [
    # [
        # host=127.0.0.1,
        # port=16379,
        # name=127.0.0.1:16379,
        # server_type=primary,
        # redis_connection=Redis<ConnectionPool<Connection<host=127.0.0.1,
        # port=16379,db=0>>>],
        # ...
    # ]
# ]

rc.set('foo', 'bar')
# True

rc.get('foo')
# b'bar'