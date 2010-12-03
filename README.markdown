Python queue implemented on top of Redis
===========================================

Requires:

* Redis 2.0+
* Newest version of [redis-py](http://github.com/andymccurdy/redis-py)
* [redis_wrap](http://pypi.python.org/pypi/redis_wrap)

You can also quick install it from [PyPi](http://pypi.python.org/pypi/redis_simple_queue):
    
* $ sudo easy_install redis_wrap
* $ sudo easy_install redis_simple_queue


Examples
========

Example of using the queue:

    from redis_simple_queue import *

    delete_jobs('tasks')

    put('tasks', '42')

    assert 'tasks' in get_all_queues()
    assert queue_stats('tasks')['queue_size'] == 1

    assert reserve('tasks') == '42'
    assert queue_stats('tasks')['queue_size'] == 0
