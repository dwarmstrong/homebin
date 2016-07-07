#!/usr/bin/env python
# See: * https://docs.python.org/2/library/datetime.html

from datetime import datetime, date

msg = """
(O< .: How many days until ...
(/)_
"""
print(msg)

def days_until(year, month, day):
    """ How many days until: yyyy mm dd """
    d0 = date.today()
    d1 = date(year, month, day)
    num = d1 - d0
    return num.days

futureDate = raw_input('Enter future date YYYY-MM-DD > ').split('-')
yyyy, mm, dd = int(futureDate[0]), int(futureDate[1]), int(futureDate[2])
dateCalc = date(yyyy, mm, dd).strftime("%A %B %d %Y")
print('{} days until {}.').format(days_until(yyyy, mm, dd), dateCalc)
