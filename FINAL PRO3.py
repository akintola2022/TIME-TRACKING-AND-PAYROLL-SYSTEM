# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:02:05 2022

@author: afagbenro
"""
#FINAL PROJECT SDEV140 (Time tracking and payroll system)

#The project is to develop and implement a new time tracking and payroll system,
#that will allow the staff to log in from anywhere on the network. 
#Each department of the organization is to monitor their staff's time tracking. 
#There will be an option for a manager to correct information once the employee has accepted it. 
#There will also be security for logging in and a manager-level login.  
#This time tracking information will feed into the payroll system.

 
#TIME TRACKING
 
#User Login detail (username and password)
#Time punch (clock -in, clock-out)

import validate

data = [0.0, 1.0,]
validate(data, float)
print()
Username =str(input('Enter username: '))
Password =str(input('Enter password: '))
Employee_name = str(input('Enter full name: first name, Last name '))
print()

#Set Time_punch  = (clock-in/clock-out)

start_time = float(input('clock-in time:'))
Stop_time = float(input('clock-out time:'))
print()
# Named constants to represent the base hours and
# the overtime multiplier.

BASE_HRS = 40      # Base hours per week
OT_MULTIPLIER = 1.5  # Overtime multiplier
 
# Get the hours worked and the hourly pay rate.
number_of_hrs_worked  = float(input('Enter total number of hours worked weekly: '))
pay_rate = float(input('Enter the hourly pay rate: '))
overtime_hours = number_of_hrs_worked - BASE_HRS
print()
# Calculate and display the gross pay.
 
if number_of_hrs_worked  > BASE_HRS:

# Calculate the amount of overtime pay.
 overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

 print('*****************************************')
# Calculate the gross pay.
 gross_pay = BASE_HRS * pay_rate + overtime_pay
else: 
 gross_pay = BASE_HRS * pay_rate
print() 
Fed = int(gross_pay * 0.04)
 
state_tax = (gross_pay * 0.012)
 
county_tax = (gross_pay * 0.007)
    
Income_Taxes = Fed + state_tax + county_tax
 
#Other deductions
medical = (gross_pay * 0.023 )
dental =(gross_pay * 0.05)
vision = (gross_pay * 0.010)
Deductions = Income_Taxes + medical + dental + vision

Net_pay = gross_pay - Deductions
     
     
# Display the paysturb.
print("GLOBE INDUSTRIES....It's all about pipe")
print("---------------------------------------------------")
print(f'Paysturb for: {Employee_name}\n')
print(f'Login detail is {Username}: password is *******')
print(f'You clocked in at {start_time:,.2f}am.')
print(f'You clocked out at {Stop_time:,.2f}pm.')
print(f'Your overtime is {overtime_hours:,.1f} hours.')
print()
print(f'Fed:{Fed:,.2f}\n')
print(f'state tax: {state_tax:,.2f}\n')
print(f'county tax:{county_tax:,.2f}\n')
print(f'Income Taxes: {Income_Taxes:,.2f}\n')
print(f'Deductions: {Deductions:,.2f}\n')
print(f'The gross pay is ${gross_pay:,.2f}.    Your Netpay:${Net_pay:,.2f}')



