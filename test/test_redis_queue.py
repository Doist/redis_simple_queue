from redis_simple_queue import *

def test_basic():
    delete_jobs('tasks')

    put('tasks', '42')

    assert 'tasks' in get_all_queues()
    assert queue_stats('tasks')['queue_size'] == 1

    assert reserve('tasks') == '42'
    assert queue_stats('tasks')['queue_size'] == 0

if __name__ == '__main__':
    test_basic()
