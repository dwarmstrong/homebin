#!/usr/bin/env python3
#
# Description: Convert pounds to kilograms.
# Usage: lbs2kg [number]
import sys

pounds = float(sys.argv[1])
kilograms = pounds * 0.4535924
print(f"{pounds}lbs = {kilograms:.1f}kg")
