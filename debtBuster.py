#!/usr/bin/env python

# Created for MITx 6.00.1 - Problem Set 2 Part 3 - Using Bisection Search

msg = """
(O< .: Find the smallest monthly payment to the cent such that we can pay off
(/)_   a debt within n months.

"""

print(msg)
b = float(raw_input('Balance owing? > '))
ub = b # unpaid balance
n = int(raw_input('Pay off the entire balance within how many months? > '))
air = float(raw_input('Annual interest rate (e.g 18% = 0.18)? > '))
mir = air / 12.0 # monthly interest rate
low = b / n # monthly payment lower bound
high = (b * (1 + mir)**n) / float(n)
epsilon = 0.01

while abs(ub) >= epsilon:
    ub = b
    ans = (high + low) / 2.0
    for m in range(n):
        ub = (ub - ans) + ((ub - ans) * mir)
    if ub < epsilon:
        high = ans
    else:
        low = ans

print('Lowest monthly payment: {:.2f}').format(round(ans, 2))
print('Total paid out: {:.2f}').format(round(ans, 2) * n)
