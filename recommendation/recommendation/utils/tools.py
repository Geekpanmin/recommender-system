import logging
import threading
import traceback
from functools import wraps


def synchronized(func):
    func.__lock__ = threading.Lock()

    @wraps(func)
    def lock_func(*args, **kwargs):
        with func.__lock__:
            res = func(*args, **kwargs)
        return res

    return lock_func


def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance


def try_catch_with_logging(default_response=None):
    def out_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except Exception:
                res = default_response
                logging.error(traceback.format_exc())
            return res

        return wrapper

    return out_wrapper
