#!/usr/bin/env python3

import argparse
from datetag import DateTag

description = (
    'Retrieve weight measurements and dates they were recorded from <source>.')
# Search for strings that match pattern.
match_pattern = '(20\d\d-\d\d-\d\dT\d\d:\d\d)\n(:weight:\s\d\d.\d)'

def get_arguments():
    parser = argparse.ArgumentParser(description=f'{description}')
    # argparse includes a built-in '-h', '--help' option that
    # auto-generates a helpful tip derived from my code
    #
    # option has required argument
    parser.add_argument('-o', '--output', help='save data to file')
    # standalone option (boolean type)
    parser.add_argument(
        '-q', '--quiet', help='do not display output', action='store_true')
    parser.add_argument(
        '-r', '--raw', help='display list of matching patterns', 
        action='store_true')
    parser.add_argument(
        '-s', '--scatter', help='display a scatter plot', action='store_true')
    # positional argument (required -- saved as a key-value pair)
    parser.add_argument('source', help='data source file')
    # create a data object that contains a summary of all arguments
    # that the function has parsed
    arguments = parser.parse_args()
    return arguments

# Command line arguments.
args = get_arguments()
source_file = f'{args.source}' # required

# Dates and weights object
w = DateTag(source_file, match_pattern)

# Search source for matching patterns and return a list.
match_list = w.make_list()

# Add list of items to dictionary as key-value pairs using string slices. Key
# is 'item[0][<k_start>:<k_end>]' and 'item[1][<v_start>:<v_end>]' as value.
k_start = 0
k_stop = 10
v_start = -4
v_stop = None   # when slicing to the end in a variable, use None as endpoint
my_dict = w.list_to_dictionary(match_list, k_start, k_stop, 
                v_start, v_stop)

# Convert dictionary to tabular data.
my_table = w.dict_to_tab(dictionary=my_dict, date_column='Date', 
    measure_column='Weight')

# Generate scatter plot for display.
if args.scatter:
    w.make_scatter(data_frame=my_table, title='Dates and Weights(kg)', 
        xlabel='Date', ylabel='Weight')

# Save data to file in JSON format.
if args.output:
    save_file = f'{args.output}.json'
    w.save_data(my_dict, save_file)
else:
    save_file = '<not saved>'

# Display output to screen if '--quiet' is not set to True.
if not args.quiet:
    if args.raw:
        to_display = match_list
    else:
        to_display = my_table
    print(to_display)
    # Find the most recent value, maximum value, and minimum value and the 
    # dates they were recorded.
    new_vd = w.value_date_new(my_dict)
    max_vd = w.value_date_max(my_dict)
    min_vd = w.value_date_min(my_dict)
    # Find the average value.
    avg_v = w.value_average(my_dict)
    # Display stats:
    #
    # * number of pattern matches
    print("\nItems: " + str(len(to_display)) + " matches.")
    #
    # * average weight
    print(f"Average weight: {avg_v}kg")
    #
    # * maximum weight and date(s) recorded
    max_v = [v for v in max_vd.values()]
    print(f"Maximum weight: {max_v[0]}kg recorded on", end="")
    for k in max_vd.keys():
        print("", k, end="")
    print(".")
    #
    # * minimum weight and date(s) recorded
    min_v = [v for v in min_vd.values()]
    print(f"Minimum weight: {min_v[0]}kg recorded on", end="")
    for k in min_vd.keys():
        print("", k, end="")
    print(".")
    #
    # * save file
    print(f"Contents saved to {save_file}.")
