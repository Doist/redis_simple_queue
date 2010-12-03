#!/usr/bin/env python
# Copyright (c) 2007 Qtrac Ltd. All rights reserved.
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

import os
from setuptools import setup

setup(name='redis_simple_queue',
      version = '1.0',
      author="amix",
      author_email="amix@amix.dk",
      url="http://www.amix.dk/",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      packages=['redis_simple_queue', 'test'],
      platforms=["Any"],
      license="BSD",
      keywords='redis queue',
      description="Python queue implemented on top of Redis.",
      long_description="""\
redis_simple_queue
---------------

redis_simple_queue implements a queue on top of Redis.

Requires:

* Redis 2.0+
* Newest version of redis-py http://github.com/andymccurdy/redis-py
* redis_wrap http://pypi.python.org/pypi/redis_wrap

Examples
----------

Example of using the queue::

    from redis_simple_queue import *

    delete_jobs('tasks')

    put('tasks', '42')

    assert 'tasks' in get_all_queues()
    assert queue_stats('tasks')['queue_size'] == 1

    assert reserve('tasks') == '42'
    assert queue_stats('tasks')['queue_size'] == 0

Copyright: 2010 by amix
License: BSD.""")
