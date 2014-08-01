#!/usr/bin/env python
# encoding: utf-8

"""
    use a global dict to store the events, 
    and here put event related operations wrapper
    ~~~~~~~~
    event.py
"""

from gevent.event import AsyncResult
from .errors import (
    EventKeyAlreadyExisted,        
    EventKeyTypeError,
)

__all__ = [
    'set_event',
    'get_event',
    'init_event',
    'register_event'
]

EVENT_ITEMS = {}

def set_event(name, value):
    """
    @name   string, event name
    @value  any,    event value
    @return boolean the set status
    """
    if not isinstance(name, basestring):
        raise EventKeyTypeError

    global EVENT_ITEMS
    if EVENT_ITEMS.has_key(name):
        EVENT_ITEMS[name].set(value)
        return True
    return False

def register_event(name, value=None):
    if not isinstance(name, basestring):
        raise EventKeyTypeError

    global EVENT_ITEMS
    if EVENT_ITEMS.has_key(name):
        raise EventKeyAlreadyExisted
    
    EVENT_ITEMS[name] = AsyncResult()
    if value is not None:
        set_event(name, value)

def get_event(name):
    global EVENT_ITEMS
    return EVENT_ITEMS.get(name, None)

def init_event(name):
    """
    @name string event name
    """
    if not isinstance(name, basestring):
        raise EventKeyTypeError

    global EVENT_ITEMS
    EVENT_ITEMS[name] = AsyncResult()

if __name__ == '__main__':
    register_event('What', 1)
    print get_event('What')
