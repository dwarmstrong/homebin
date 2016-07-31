import logging, os, re
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

logging.basicConfig(level=logging.DEBUG,
        format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

msg = '''
(O< .: Collect dates (x_axis) and corresponding y measurements (y_axis)
(/)_   from logfile.
'''

def date_and_y(logfile, savefile, regex_date, regex_y):
    '''Search for regex_date and regex_y'''
    f = logfile
    f_out = savefile
    dateObj = re.compile(r'{}'.format(regex_date))
    yObj = re.compile(r'{}'.format(regex_y))
    if os.path.exists(f):
        with open(logfile, 'r') as f, open(savefile, 'w') as f_out:
            searchLines = f.readlines()
            for i in searchLines:
                if dateObj.search(i) != None or yObj.search(i) != None:
                    if dateObj.search(i) != None:
                        mo = dateObj.search(i)
                    else:
                        mo = yObj.search(i)
                    f_out.write(mo.group() + '\n')

def match_date_and_y(logfile, regex_date, regex_y):
    '''Match date(x) with corresponding y or remove dates with no matches'''
    with open(logfile, 'r') as f:
        searchLines = f.readlines()
    with open(logfile, 'w') as f:
        dateObj = re.compile(r'{}'.format(regex_date))
        yObj = re.compile(r'{}'.format(regex_y))
        for index, line in enumerate(searchLines):
            if yObj.search(line) != None:
                f.write(line) # regex_y match
            elif searchLines[index] == searchLines[-1]:
                break # prevent 'IndexError: list index out of range' 
            elif yObj.search(searchLines[index+1]) != None:
                f.write(line) # regex_date ... if next line matches regex_y

def gen_list(logfile, regex):
    '''Create a list from regex match items'''
    with open(logfile, 'r') as f:
        searchLines = f.readlines()
        xy_list = []
        reObj = re.compile(r'{}'.format(regex))
        for line in searchLines:
            if reObj.search(line) != None:
                mo = reObj.search(line)
                xy_list.append(mo.group())
        return xy_list

def str_to_float_list(str_list):
    '''Convert list of strings to floating point items - in reverse order'''
    float_list = [i for i in reversed(str_list)]
    return float_list

def last_day_of_month():
    '''Calculate the last day of the current month'''
    # Get the first day of the *next* month and subtract one day
    nmonth = dt.date.today() + dt.timedelta(days=32)
    lday = nmonth.replace(day=1) - dt.timedelta(1)
    return lday

def gen_date_y_graph(graph_title, date_axis, startdate, y_axis, y_label, y_marker, savefile):
    '''Generate a graph using a list of dates as x_axis'''
    x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in date_axis]
    y = y_axis
    plt.xticks(rotation=70)
    plt.plot(x, y, y_marker)
    ymd = startdate.split('-') # startdate as 'YYYY-M(M)-D(D)'
    start_date = dt.datetime(int(ymd[0]),int(ymd[1]),int(ymd[2]))
    end_date = last_day_of_month()
    logging.debug('Current axis: {}'.format(plt.axis()))
    logging.debug('Start date: {}'.format(start_date))
    logging.debug('End date: {}'.format(end_date)) 
    plt.xlim(start_date, end_date)    
    plt.title(graph_title)
    plt.ylabel(y_label)
    #
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gca().xaxis.set_minor_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_minor_formatter(mdates.DateFormatter('%m'))
    plt.gca().format_xdata = mdates.DateFormatter('%Y-%m-%d')
    plt.gcf().autofmt_xdate()
    #
    plt.grid(True)
    plt.show()
    #plt.savefig(savefile)
