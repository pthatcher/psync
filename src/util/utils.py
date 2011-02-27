# Copyright 2006 Uberan - All Rights Reserved

import threading
import time
    
class Clock:
    def unix(_):
        return int(time.time())

    def unix_fine(_):
        return time.time()

def groupby(vals, key = None, into = None):
    group_by_key = {}
    for val in vals:
        group = group_by_key.setdefault(key(val), [])
        group.append(val)

    if into is not None:
        for key in group_by_key:
            group_by_key[key] = into(group_by_key[key])

    return group_by_key

# like dct.setdefault(key, get_val(*args, **kargs)), except lazy
def setdefault(dct, key, get_val, *args, **kargs):
    try:
        return dct[key]
    except KeyError:
        val = get_val(*args, **kargs)
        dct[key] = val
        return val
    
def partition(vals, predicate):
    trues, falses = [], []
    for val in vals:
        (trues if predicate(val) else falses).append(val)
    return trues, falses

def flip_dict(dct):
    return dict((v, k) for (k, v) in dct.iteritems())

# If you have an enum of types and a record where the first value is
# the type, this will let you say Record.type1(arg2, arg3).  It sounds
# tricky, but it's really handy.
def type_constructors(types):
    def add_type_constructor(cls, type):
        @classmethod
        def type_constructor(cls, *args):
            return cls(type, *args)

        setattr(cls, type.name, type_constructor)

    def add_type_constructors(cls):
        for type in types:
            add_type_constructor(cls, type)
        return cls

    return add_type_constructors

def start_thread(func, name = None, isdaemon = True):
    thread = threading.Thread(target = func)
    if name is not None:
        thread.setName(name)
    thread.setDaemon(isdaemon)
    thread.start()
    return thread

