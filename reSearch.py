#!/usr/bin/env python3
import argparse, re, os
from binaryornot.check import is_binary # sudo apt install python3-binaryornot

msg = '''
(O< .: Find matches for REGEX(s) in SOURCE
(/)_
'''

parser = argparse.ArgumentParser(description=msg, 
                                formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("REGEX", nargs="+", help="search for REGEX pattern")
parser.add_argument("SOURCE", help="file(s) to search")
parser.add_argument("-o", "--output", help="save results to file OUTPUT")
parser.add_argument("-q", "--quiet", help="no output to console",
                    action="store_true")
args = parser.parse_args()

def compile_regex(items):
    """Create regex object"""
    searchFor = ""
    for i in items:
        searchFor += "|" + i
    regexObj = re.compile(r'{}'.format(searchFor[1:]))
    return regexObj


def search_list(source):
    """Create list of items to search"""
    if os.path.exists(source):
        f = open("{}".format(source), "r")
        lines = []
        for line in f:
            lines.append(line)
        f.close()
        return lines
    else:
        return None

def find_match(regex, source):
    """Process regex match to output"""
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

def regex_space(search_here, things_of_interest):
    """Search file(s) for regex matches"""
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

regex_space(args.SOURCE, args.REGEX)
