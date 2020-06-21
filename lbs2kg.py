#!/usr/bin/env python3
#
# Convert pounds to kilograms.
import sys

# Usage: lbs2kg [number]
pounds = float(sys.argv[1])
kilograms = pounds * 0.4535924
print(f"{pounds}lbs = {kilograms:.1f}kg")
