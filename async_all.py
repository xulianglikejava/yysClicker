# 作者: xl
# 时间: 2022/11/5 22:28
from threading import Thread
from time import sleep


def async_call(fn):
    def wrapper(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()

    return wrapper




