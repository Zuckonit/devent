#!/usr/bin/env python
# encoding: utf-8

"""

    timer event
    ~~~~~~~~~~~~
    greenlets.py
"""

import signal
import gevent
from .event import set_event, get_event
from .errors import NotCallAble


class EventWatcher(object):
    def __init__(self, event_name, interval, callback, *args, **kwargs):
        super(EventWatcher, self).__init__()
        self.interval = interval
        self.run_status = True
        self.event_name = event_name
        self.callback = callback
        if not callable(self.callback):
            raise NotCallAble

        self.args = args
        self.kwargs = kwargs

        gevent.signal(signal.SIGQUIT, self.end)
        gevent.signal(signal.SIGINT, self.end)
        gevent.signal(signal.SIGTERM, self.end)

    def run(self):
        while self.run_status:
            event_val = self.callback(*self.args, **self.kwargs)
            set_event(self.event_name, event_val)
            #print get_event(self.event_name)  #here is for debug
            gevent.sleep(self.interval)

    def start(self):
        gevent.joinall([
            gevent.spawn(self.run)    
        ])

    def end(self):
        self.run_status = False


if __name__ == '__main__':
    def a():
        return 100
    
    #--------------------------------
    #give initial value for event 'a'
    #--------------------------------
    from decorators import register
    @register('a')
    def b():
        return 1
    b()
    
    #--------------------------------
    #start timer
    #--------------------------------
    try:
        event_watcher = EventWatcher('a', 1, a)
    except NotCallAble:
        print 'function %s is not callable' % a.__name__
    else:
        event_watcher.start()
