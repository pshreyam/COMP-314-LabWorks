from functools import wraps
import time


def timer(f):
    """Return the execution time (in microseconds) along with the result of each function."""
    @wraps(f)
    def wrap(*args, **kwargs):
        t1 = time.perf_counter()
        result = f(*args, **kwargs)
        t2 = time.perf_counter()
        duration = (t2 - t1) * 1000 * 1000
        return {
            "duration": duration,
            "result": result
        }
    return wrap
