#!/usr/bin/env python3
#
description = ('Given a loan at a fixed rate of interest, calculate the ' 
        'total amount paid over the life of a loan.\n')
extra_payment_start = 0
extra_payment_end = 0
total_paid = 0.0
total_payments = 0

print(description)

# conditions
principal = float(input("Amount of loan?  "))
rate = float(input("Rate of interest?  "))
period = input("Are payments monthly or weekly? [month|week]  ")
payment = float(input("Amount of payment?  "))
extra = input(f"Do you wish to make an extra {period}ly payment? [yes|no]  ")
if extra.lower() == 'yes':
    extra_payment = float(input("Amount of extra payment?  "))
    extra_payment_start = int(input(f"Extra payment start {period}?  "))
    extra_payment_end = int(input(f"Extra payment end {period}?  "))
    
# installments per year
if period.lower() == 'month':
    period = 12
else:
    period = 52

# calculate
while principal > 0:
    x = principal * (1+rate/period)
    total_payments += 1
    if (total_payments >= extra_payment_start and 
            total_payments <= extra_payment_end):
        principal = x - (payment + float(extra_payment))
        total_paid += (payment + float(extra_payment))
    else:
        principal = x - payment
        total_paid += payment
    if principal < 0:
        total_paid = total_paid - abs(principal)
        principal = 0
    print(f'{total_payments}  {total_paid:0.2f}  {principal:0.2f}')

print(f'\nTotal paid = {total_paid:0.2f}')
print(f'Total payments = {total_payments}')
