#!/usr/bin/env python3
import argparse, re, os, logging, shutil, datetime
from binaryornot.check import is_binary # apt install python3-binaryornot

logging.basicConfig(level=logging.DEBUG, 
        format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

msg = '''
(O< .: Find matches for REGEX(s) in SOURCE
(/)_
'''

example0 = ("reSearch.py -q -o ~/log/dateAndWeight.txt '^201[4-9]-\d\d-\d\d' " 
    "'^#weight\s\d\d...?' ~/log/daily.log")
use_example = '''
EXAMPLES
    Here are some examples of how I use reSearch.py ...

    To retrieve a list of weight measurements and dates from my personal logfile
    and save to an output file:

        {}
'''.format(example0)

parser = argparse.ArgumentParser(description=msg, epilog=use_example, 
        formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("REGEX", nargs="+", help="search for REGEX pattern")
parser.add_argument("SOURCE", help="file(s) to search")
parser.add_argument("-o", "--output", help="save results to file OUTPUT")
parser.add_argument("-q", "--quiet", help="no output to console", 
        action="store_true")
parser.add_argument("-s", "--sub", help="replace regex match with SUB")
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
        f = open(source, 'r')
        f_clone = f.readlines()
        f.close()
        return f_clone
    else:
        logging.debug('End of search_list({})'.format(source))
        return None

def switcheroo(pattern, source):
    """Replace pattern with new_pattern"""
    t = datetime.datetime.today()
    bak = (source + '.' + t.strftime("%Y-%m-%dT%H.%M.%S.%f") + '.bak')
    shutil.copyfile(source, bak)
    logging.debug("Backup " + source + " to " + bak)
    f = open(bak, 'r')
    f_clone = f.readlines() # returns a list, as opposed to read() which returns
                            # file as string (not useful for position regex)
    logging.debug('Load and read ' + bak)
    f.close()
    replace = (r'{}'.format(args.sub))
    logging.debug("Replace '{}' with '{}' in "
            .format(args.REGEX, args.sub) + source)
    f_out = open(source, 'w')
    for i in f_clone:
        if pattern.search(i) == None:
            f_out.write(i)
        else:
            f_string = (pattern.sub(replace, i))
            f_out.write(f_string)
    logging.debug("Write and save changes.")
    f_out.close()

def find_match(regex, source):
    """Process regex match to output"""
    logging.debug('Start of find_match({}, {})'.format(regex, source))
    findObj = compile_regex(regex)
    lines = search_list(source)
    str_regex = ("Regex patterns to match: " + str(args.REGEX) + "\n")
    str_source = ("Match results for \'" + source + "\':\n")
    if not args.quiet:
        print(str_regex + str_source)
    if args.output:
        f_out = open("{}".format(args.output), "a")
        f_out.write(str_regex)
        f_out.write(str_source)
        f_out.close()
    if args.sub:
        switcheroo(findObj, source)
    for match in lines:
        if findObj.search(match) == None:
            pass
        else:
            mo = findObj.search(match)
            if args.output:
                f_out = open("{}".format(args.output), "a")
                f_out.write(mo.group() + "\n")
                f_out.close
            if not args.quiet:
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
