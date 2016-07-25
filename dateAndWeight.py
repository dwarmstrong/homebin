#!/usr/bin/env python3

import logging
from dateAndY import gen_date_and_y

msg = '''
(O< .: Collect dates (x_axis) and corresponding weight measurements (y_axis)
(/)_   from my daily logfile.
'''
dailyLog = "/home/dwa/share/log/daily.log"
weightLog = "/home/dwa/share/log/weight.log"

if __name__ == '__main__':
    gen_date_and_y(dailyLog, weightLog, '^201[4-9]-\d\d-\d\d', '^#weight\s\d\d...?')
