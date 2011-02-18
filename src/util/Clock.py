# Copyright 2006 Uberan - All Rights Reserved

class Clock:
    def now_unix(self):
        return time.time()

    def run_time(clock, func, *args, **kargs):
        before = clock.now_unix()
        result = func(*args, **kargs)
        after = clock.now_unix()
        return (result, after-before)
