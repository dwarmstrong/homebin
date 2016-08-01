#!/usr/bin/env python3

import argparse, logging, re
from dateAndY import (date_and_y, match_date_and_y, gen_list, 
        str_to_float_list, gen_date_y_graph)

logging.basicConfig(level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

msg = '''
(O< .: Collect dates (x_axis) and corresponding weight measurements (y_axis)
(/)_   from my daily logfile and write to a new logfile + generate a graph.
'''

dailyLog = "/home/dwa/share/log/daily.log"
weightLog = "/home/dwa/share/log/dateAndWeight.log"
date_regex = "^201[4-9]-\d\d-\d\d"
weight_regex = "^\d\d\.\d"

parser = argparse.ArgumentParser(description=msg, 
        formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-n", "--nograph", 
        help="create logfile but skip the graph", action="store_true")
args = parser.parse_args()

def weight_cleanup(logfile):
    '''Run any metric conversions and remove tags'''
    with open(logfile, 'r') as f:
        searchLines = f.readlines()
    with open(logfile, 'w') as f:
        lbs = re.compile(r'^(#weight\s)(\d\d\d\.\d)')
        kg = re.compile(r'^(#weight\s)(\d\d\.\d)')
        for line in searchLines:
            # Convert lbs to kg and remove tags
            if lbs.search(line) != None:
                mo = lbs.search(line)
                k = float(mo.group(2)) / 2.2046 # metric conversion
                line = re.sub(r'#weight\s\d\d\d\.\d', str(round(k, 1)), line)
                f.write(line)
            # Remove tags
            elif kg.search(line) != None:
                mo = kg.search(line)
                line = re.sub(r'#weight\s\d\d\.\d', str(mo.group(2)), line)
                f.write(line)
            else:
                f.write(line)

if __name__ == '__main__':
    # Search for dates and weight measurements and output to weightLog
    date_and_y(dailyLog, weightLog, date_regex, '^#weight\s\d\d...?')
    weight_cleanup(weightLog)
    # Match date with corresponding weight or remove dates with no matches
    match_date_and_y(weightLog, date_regex, weight_regex)
    # List of dates
    dates = str_to_float_list(gen_list(weightLog, date_regex))
    logging.debug(dates)
    # List of weights
    weights = str_to_float_list(gen_list(weightLog, weight_regex))
    logging.debug(weights)
    logging.debug('Dates: ' + str(len(dates)))
    logging.debug('Weights: ' + str(len(weights)))
    # Generate graph
    if not args.nograph:
        gen_date_y_graph('Dates and Weights',           # Title
                        dates, '2014-1-1',              # x_axis 
                        weights, 'Weight (kg)', 'o',    # y_axis
                        'dateAndWeight.png')            # Save to...
    logging.debug('End of program')
