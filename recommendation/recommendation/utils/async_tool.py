import threading


def apply_async(func, *args, **kwargs):
    thr = threading.Thread(target=func, args=args, kwargs=kwargs)
    thr.start()
    return thr
