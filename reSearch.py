#!/usr/bin/env python3
import argparse, re, os, logging
from binaryornot.check import is_binary # apt install python3-binaryornot

logging.basicConfig(level=logging.DEBUG, 
        format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

msg = '''
(O< .: Find matches for REGEX(s) in SOURCE
(/)_
'''

use_example = '''
example: reSearch.py -q -o dates.txt '^201[4-9]' ~/daily.log
            Search file ~/daily.log for all lines that start with
            2014 to 2019 and output results to dates.txt
'''

parser = argparse.ArgumentParser(description=msg, epilog=use_example, 
        formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("REGEX", nargs="+", help="search for REGEX pattern")
parser.add_argument("SOURCE", help="file(s) to search")
parser.add_argument("-o", "--output", help="save results to file OUTPUT")
parser.add_argument("-q", "--quiet", help="no output to console", 
        action="store_true")
args = parser.parse_args()

def compile_regex(items):
    """Create regex object"""
    logging.debug('Start of compile_regex({})'.format(items))
    searchFor = ""
    for i in items:
        searchFor += "|" + i
    regexObj = re.compile(r'{}'.format(searchFor[1:]))
    logging.debug('End of compile_regex({})'.format(items))
    return regexObj


def search_list(source):
    """Create list of items to search"""
    logging.debug('Start of search_list({})'.format(source))
    if os.path.exists(source):
        f = open("{}".format(source), "r")
        lines = []
        for line in f:
            lines.append(line)
        f.close()
        logging.debug('End of search_list({})'.format(source))
        return lines
    else:
        logging.debug('End of search_list({})'.format(source))
        return None

def find_match(regex, source):
    """Process regex match to output"""
    logging.debug('Start of find_match({}, {})'.format(regex, source))
    findObj = compile_regex(regex)
    lines = search_list(source)
    str_regex = ("Regex patterns to match: " + str(args.REGEX) + "\n")
    str_source = ("Match results for \'" + source + "\':\n")
    print(str_regex + str_source)
    if args.output:
        results = args.output
        o = open("{}".format(results), "a")
        o.write(str_regex)
        o.write(str_source)
        o.close
    for match in lines:
        if findObj.search(match) == None:
            pass
        else:
            mo = findObj.search(match)
            if args.output:
                o = open("{}".format(results), "a")
                o.write(mo.group() + "\n")
                o.close
            if args.quiet:
                pass
            else:
                print(mo.group())
    logging.debug('End of find_match({}, {})'.format(regex, source))

def regex_space(search_here, things_of_interest):
    """Search file(s) for regex matches"""
    logging.debug('Start of regex_space({}, {})'.format(search_here, 
        things_of_interest))
    s = search_here
    t = things_of_interest
    if os.path.exists(s):
        if os.path.isdir(s):
            directory = s
            files = os.listdir(s)
            for i in files:
                if os.path.isfile(i):
                    f = os.path.abspath(os.path.join(directory, i))
                    if not is_binary(f):
                        find_match(t, f)
        else:
            f = os.path.abspath(s)
            if not is_binary(f):
                find_match(t, f)
    else:
        raise Exception("Source '" + search_here + "' not found.")
    logging.debug('End of regex_space({}, {})'.format(search_here, 
        things_of_interest))

try:
    regex_space(args.SOURCE, args.REGEX)
except Exception as err:
    print('Arrgh...an exception: ' + str(err))

logging.debug('End of program')
