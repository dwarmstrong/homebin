#!/usr/bin/env python
import time

msg = """
(O< .: Measure clock time for this device to count from 0 to x in
(/)_   increments of 1.
"""
print(msg)
max = int(raw_input('Enter a positive integer for x > '))
start = time.time()
i = 0
while i < max:
    i += 1
end = time.time()
elapsed = end - start
print('Time elapsed: {:.3f} '.format(elapsed) + 'seconds')
