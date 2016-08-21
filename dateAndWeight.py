#!/usr/bin/env python3

import argparse, logging, re
from os.path import expanduser
from dateAndY import Logfile, GenerateGraph

logging.basicConfig(level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

msg = """
(O< .: Collect dates (x_axis) and weight measurements (y_axis) from my
(/)_   daily logfile and write to a new logfile + generate a graph.
"""

parser = argparse.ArgumentParser(description=msg, 
        formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-n", "--nograph", 
        help="create logfile but skip the graph", action="store_true")
args = parser.parse_args()

home = expanduser("~")
dailyLog = home + "/share/log/daily.log"
weightLog = home + "/share/log/dateAndWeight.log"
date_regex = "^20[0-9][0-9]-\d\d-\d\d"
weight_regex = "^\d\d\.\d"

def weight_cleanup(logfile):
    """Run any metric conversions and remove tags."""
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
    ## Logfile
    log = Logfile(dailyLog, weightLog, date_regex)
    
    ## Search for dates and weight measurements and output to weightLog
    log.date_and_y('^#weight\s\d\d...?')
    weight_cleanup(weightLog)
    ## Match date with corresponding weight or remove dates with no matches
    log.match_date_and_y(weight_regex)
    ## Generate list of dates
    dates = log.str_to_float_list(log.gen_list(date_regex))
    logging.debug(dates)
    ## Generate list of weights
    weights = log.str_to_float_list(log.gen_list(weight_regex))
    logging.debug(weights)
    logging.debug('Dates: ' + str(len(dates)))
    logging.debug('Weights: ' + str(len(weights)))

    ## GenerateGraph
    graph = GenerateGraph('Dates and Weights',  # Title
            dates, '2014-1-1',                  # x_axis
            weights, 'Weight (kg)')             # y_axis
    
    if not args.nograph:
        graph.gen_date_y_graph('o') # 'o' y_marker
    
    logging.debug('End of program')
