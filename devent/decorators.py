#!/usr/bin/env python
# encoding: utf-8

import functools
from .event import register_event

def register(name=None):
    def wrapper(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            result_val = func(*args, **kwargs)
            key = func.__name__ if not name else name
            register_event(key, result_val)
        return _wrapper
    return wrapper

    
if __name__ == '__main__':
    @register()
    def a():
        return 1
    a()

    from event import get_event
    print get_event('a')
