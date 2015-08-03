#!/usr/bin/env python3
"""
Simple module to sleep the process for a random integer number of seconds.
"""

import random
import time

def randsleep(min = 1, max = 1, quiet = True):
    secs = random.randint(min, max)
    if not quiet:
        print("Going to sleep for", secs, \
              secs > 1 and "seconds." or "second.")
    time.sleep(secs)

def __test():
    randsleep(min = 2, max = 3, quiet = False)

if __name__ == '__main__':
    __test()
