from redis_wrap import *

def put(queue, job_data, system='default'):
    get_list(queue, system=system).append(job_data)

def reserve(queue, system='default'):
    return get_list(queue, system=system).pop()

def delete_jobs(queue, system='default'):
    get_redis(system).delete(queue)

def get_all_queues(system='default'):
    return get_redis(system).keys('*').split(' ')

def queue_stats(queue, system='default'):
    return {
        'queue_size': len(get_list(queue))
    }
