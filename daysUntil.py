#!/usr/bin/env python
# See: * https://docs.python.org/2/library/datetime.html

from datetime import datetime, date

msg = """
(O< .: How many days until: yyyy mm dd
(/)_
"""
print(msg)

def days_until(year, month, day):
    """ How many days until: yyyy mm dd """
    d0 = date.today()
    d1 = date(year, month, day)
    num = d1 - d0
    return num.days

yyyy = int(raw_input('Enter yyyy > '))
mm = int(raw_input('Enter mm > '))
dd = int(raw_input('Enter dd > '))
targetDate = date(yyyy, mm, dd).strftime("%A %B %d %Y")
print('{} days until {}.').format(days_until(yyyy, mm, dd), targetDate)
