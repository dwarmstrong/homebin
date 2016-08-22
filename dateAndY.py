"""A set of classes to support collecting dates (x_axis) and measurements
(y_axis) from a logfile and write to a new logfile and generate a graph."""

import logging, os, re
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class Logfile():
    """Read and write logfiles."""

    def __init__(self, logfile, savefile, regex_date):
        """Read a logfile, find dates, and write any matches to file."""
        self.logfile = logfile
        self.savefile = savefile
        self.regex_date = regex_date

    def date_and_y(self, regex_y):
        """Search for matching dates and regex patterns."""
        dateObj = re.compile(r'{}'.format(self.regex_date))
        yObj = re.compile(r'{}'.format(regex_y))
        if os.path.exists(self.logfile):
            with open(self.logfile, 'r') as f:
                searchLines = f.readlines()
            with open(self.savefile, 'w') as f_out:
                for i in searchLines:
                    if dateObj.search(i) != None or yObj.search(i) != None:
                        if dateObj.search(i) != None:
                            mo = dateObj.search(i)
                        else:
                            mo = yObj.search(i)
                        f_out.write(mo.group() + '\n')

    def match_date_and_y(self, regex_y):
        """Match date(x) with y or remove dates with no matches."""
        with open(self.savefile, 'r') as f:
            searchLines = f.readlines()
        with open(self.savefile, 'w') as f:
            dateObj = re.compile(r'{}'.format(self.regex_date))
            yObj = re.compile(r'{}'.format(regex_y))
            for index, line in enumerate(searchLines):
                if yObj.search(line) != None:
                    f.write(line) # regex_y match
                elif searchLines[index] == searchLines[-1]:
                    break # prevent 'IndexError: list index out of range' 
                elif yObj.search(searchLines[index+1]) != None:
                    f.write(line) # regex_date if next line matches regex_y


    def gen_list(self, regex):
        """Create a list from regex match items."""
        with open(self.savefile, 'r') as f:
            searchLines = f.readlines()
            xy_list = []
            reObj = re.compile(r'{}'.format(regex))
            for line in searchLines:
                if reObj.search(line) != None:
                    mo = reObj.search(line)
                    xy_list.append(mo.group())
            return xy_list

    def str_to_float_list(self, str_list):
        """Convert list of strings to floating points in reverse order."""
        float_list = [i for i in reversed(str_list)]
        return float_list


class GenerateGraph():
    """Generate a graph from matching items retrieved from logfile."""

    def __init__(self, graph_title, date_axis, startdate, y_axis, y_label):
        """Setup graph with a title, startdate (x_axis), and xy labels."""
        self.graph_title = graph_title
        self.date_axis = date_axis
        self.startdate = startdate
        self.y_axis = y_axis
        self.y_label = y_label

    def last_day_of_month(self):
        """Calculate the last day of the current month."""
        ## Get the first day of the *next* month and subtract one day
        nmonth = dt.date.today() + dt.timedelta(days=32)
        last_day = nmonth.replace(day=1) - dt.timedelta(1)
        return last_day

    def gen_date_y_graph(self, y_marker):
        """Generate graph using custom marker for y_axis."""
        x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in self.date_axis]
        y = self.y_axis
        plt.plot(x, y, y_marker)

        ## Chart title and label axes
        plt.title(self.graph_title)
        #plt.xlabel()   # omit ... date ticks are understood
        plt.ylabel(self.y_label)

        ## Range of x_axis (and allow y_axis to be auto-configured)
        ymd = self.startdate.split('-') # startdate as 'YYYY-M(M)-D(D)'
        start_date = dt.datetime(int(ymd[0]),int(ymd[1]),int(ymd[2]))
        end_date = self.last_day_of_month()
        plt.xlim(start_date, end_date)

        ## Grid
        plt.gca().xaxis.set_major_locator(mdates.YearLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        plt.gca().xaxis.set_minor_locator(mdates.MonthLocator())
        plt.gca().xaxis.set_minor_formatter(mdates.DateFormatter('%m'))
        plt.gca().format_xdata = mdates.DateFormatter('%Y-%m-%d')
        plt.gca().get_xaxis().set_tick_params(which='major', pad=15)
        plt.gcf().autofmt_xdate()
        plt.grid(True, which='both')

        labels = plt.gca().get_xticklabels()
        plt.setp(labels, rotation=0, ha='center', fontsize=15)
        
        plt.show()
