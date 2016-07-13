#!/usr/bin/env python3
import argparse, re, os

msg = '''
(O< .: Find matches for REGEX(s) in SOURCE
(/)_
'''

# Get command-line arguments
parser = argparse.ArgumentParser(description=msg, 
                                formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("REGEX", nargs="+", help="search for REGEX pattern")
parser.add_argument("SOURCE", help="file(s) to search")
parser.add_argument("-o", "--output", help="save results to file OUTPUT")
parser.add_argument("-q", "--quiet", help="no output to console",
                    action="store_true")
args = parser.parse_args()

pattern = args.REGEX
source = args.SOURCE
resultTxt = ""

if args.output:
    resultTxt= args.output
    print("Save regex matches to " + resultTxt)
if args.quiet:
    print("quiet turned on")
print("Regex patterns to match: " + str(pattern))
print("Source to search is " + source)

# Create regex
def searchable(items):
    lookFor = ""
    for r in items:
        lookFor += "|" + r
    lookFor = lookFor[1:]
    return lookFor

# Find matches
if os.path.exists(source):
    #print('Source ' + str(source) + ' exists.')
    #searchFile = open('{}'.format(source), 'r')
    f = open("{}".format(source), "r")
    lines = []
    for line in f:
        lines.append(line)
    f.close()
    someRegex = re.compile(r'{}'.format(searchable(pattern)))
    for match in lines:
        if someRegex.search(match) == None:
            pass
        else:
            mo = someRegex.search(match)
            print(mo.group())
else:
    print('Not found')
