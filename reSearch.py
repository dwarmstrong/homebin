#!/usr/bin/env python3
import argparse, re, os

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

print("Regex patterns to match: " + str(args.REGEX))
print("Source to search is " + str(args.SOURCE))

def compile_regex(items):
    """Create regex object"""
    searchFor = ""
    for i in items:
        searchFor += "|" + i
    regexObj = re.compile(r'{}'.format(searchFor[1:]))
    return regexObj


def search_space(source):
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
    someRegex = compile_regex(regex)
    lines = search_space(source)
    if lines == None:
        print('Source not found.')
        exit()
    for match in lines:
        if someRegex.search(match) == None:
            pass
        else:
            mo = someRegex.search(match)
            if args.output:
                resultTxt= args.output
                o = open("{}".format(resultTxt), "a")
                o.write(mo.group() + "\n")
                o.close
            if args.quiet:
                pass
            else:
                print(mo.group())

find_match(args.REGEX, args.SOURCE)
