#!/usr/bin/env python3

import argparse, logging, re
from os.path import expanduser
from dateAndY import Logfile, GenerateGraph

logging.basicConfig(level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

msg = """
(O< .: Collect dates (x_axis) and pedometer measurements (y_axis) from my
(/)_   daily logfile and write to a new logfile + generate a graph.
"""

parser = argparse.ArgumentParser(description=msg, 
        formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-n", "--nograph", 
        help="create logfile but skip the graph", action="store_true")
args = parser.parse_args()

home = expanduser("~")
dailyLog = home + "/share/log/daily.log"
stepLog = home + "/share/log/dateAndStep.log"
date_regex = "^20[0-9][0-9]-\d\d-\d\d"
step_regex = "^\d+$"

def step_cleanup(logfile):
    """Remove tags."""
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
    ## Logfile
    log = Logfile(dailyLog, stepLog, date_regex)

    ## Search for dates and pedometer measurements and output to stepLog
    log.date_and_y('^#steps\s\d{0,}')
    step_cleanup(stepLog)
    ## Match date with corresponding steps or remove dates with no matches
    log.match_date_and_y(step_regex)
    ## Generate list of dates
    dates = log.str_to_float_list(log.gen_list(date_regex))
    logging.debug(dates)
    ## Generate list of steps
    steps = log.str_to_float_list(log.gen_list(step_regex))
    logging.debug(steps)
    logging.debug('Dates: ' + str(len(dates)))
    logging.debug('Steps: ' + str(len(steps)))

    ## GenerateGraph
    graph = GenerateGraph('Dates and Steps',    # Title
            dates, '2015-1-1',                  # x_axis
            steps, 'Steps')                     # y_axis

    if not args.nograph:
        graph.gen_date_y_graph('o') # 'o' y_marker

    logging.debug('End of program')
