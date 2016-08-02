#!/usr/bin/env python3

import argparse, logging, re
from dateAndY import (date_and_y, match_date_and_y, gen_list, 
        str_to_float_list, gen_date_y_graph)

logging.basicConfig(level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

msg = '''
(O< .: Collect dates (x_axis) and corresponding pedometer measurements (y_axis)
(/)_   from my daily logfile and write to a new logfile + generate a graph.
'''

dailyLog = "/home/dwa/share/log/daily.log"
stepLog = "/home/dwa/share/log/dateAndStep.log"
date_regex = "^20[0-9][0-9]-\d\d-\d\d"
step_regex = "^\d+$"

parser = argparse.ArgumentParser(description=msg, 
        formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-n", "--nograph", 
        help="create logfile but skip the graph", action="store_true")
args = parser.parse_args()

def step_cleanup(logfile):
    '''Remove tags'''
    with open(logfile, 'r') as f:
        searchLines = f.readlines()
    with open(logfile, 'w') as f:
        step = re.compile(r'^(#steps\s)(\d{0,})')
        for line in searchLines:
            # Remove tags
            if step.search(line) != None:
                mo = step.search(line)
                line = re.sub(r'#steps\s\d{0,}', str(mo.group(2)), line)
                f.write(line)
            else:
                f.write(line)

if __name__ == '__main__':
    # Search for dates and pedometer measurements and output to stepLog
    date_and_y(dailyLog, stepLog, date_regex, '^#steps\s\d{0,}')
    step_cleanup(stepLog)
    # Match date with corresponding steps or remove dates with no matches
    match_date_and_y(stepLog, date_regex, step_regex)
    # List of dates
    dates = str_to_float_list(gen_list(stepLog, date_regex))
    logging.debug(dates)
    # List of steps
    steps = str_to_float_list(gen_list(stepLog, step_regex))
    logging.debug(steps)
    logging.debug('Dates: ' + str(len(dates)))
    logging.debug('Steps: ' + str(len(steps)))
    # Generate graph
    if not args.nograph:
        gen_date_y_graph('Dates and Steps',     # Title
                        dates, '2015-1-1',      # x_axis 
                        steps, 'Steps', 'o',    # y_axis
                        'dateAndStep.png')      # Save to...
    logging.debug('End of program')
