#!/usr/bin/env python3
# Written by: Daniel Wayne Armstrong - https://www.circuidipity.com

name = 'datenum.py'
description = 'retrieve dates and measurements from FILE that match PATTERN'

# Provide config file as argument, example: `datenum.py config_name.conf`).
# Alternately, provide a directory to process multiple config files as a
# batch ('-b CONFIG_DIR' option).
#
# A config file at minimum will contain:
# * location of FILE to be searched
# * date pattern
# * an associated numerical pattern

# Search for matching date + number pairs and output results as:
# * two column datasheet (default)
# * graph (option)
# * stdout (option)
#
# Example of use: Output weight data recorded in a logfile over a specified
# time period by seeking out dates and their matching measurements.
