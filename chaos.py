#!/usr/bin/env python
# File: chaos.py -- A simple program illustrating chaotic behaviour
# Link: https://github.com/vonbrownie/homebin

def main():
    print("(O< .: This program illustrates a chaotic function by comparing " +
        "2 values.")
    print("(/)_")
    v0 = float(input("First value: Enter a number between 0 and 1 > "))
    v1 = float(input("Second value: Enter a number between 0 and 1 > "))
    n = int(input("How many numbers should I print?: "))
    print("\ninput\t" + str(v0) + "\t\t\t" + str(v1))
    print("-" * 51)
    for i in range(n):
        v0 = 3.9 * v0 * (1-v0)
        v1 = 3.9 * v1 * (1-v1)
        print("\t{0:0.16f}\t{1:00.16f}".format(v0, v1))

main()
