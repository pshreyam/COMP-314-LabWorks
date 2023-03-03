import time
from functools import wraps


def timer(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        t1 = time.time_ns()
        f(*args, **kwargs)
        t2 = time.time_ns()
        duration = t2 - t1
        return duration
    return wrap
