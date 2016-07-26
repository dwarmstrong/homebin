import os, re

msg = '''
(O< .: Collect dates (x_axis) and corresponding y measurements (y_axis)
(/)_   from logfile.
'''

def gen_date_and_y(logfile, savefile, regex_date, regex_y):
    '''Search for date and y'''
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
