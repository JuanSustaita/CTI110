# This program is to help other people budget properly while traveling
# Date: Feb 15, 2023
# CTI-110 P1HW2 - Travel Expense
# Juan Sustaita
#

print('This program calculates and displays travel expenses')

budget = float(input('Enter Budget: '))
destination = input('Enter your travel destination: ')
gas = float(input('How much do you think you will spend on gas? '))
accomodation = float(input('Approximately, how much will you need for accomodation/hotel? '))
food = float(input('Last, how much do you need for food? '))
remaining = budget - gas - accomodation - food

print('------------Travel Expenses------------')

print('Location: ' + destination)
print('Initial Budget: ' + str(budget))
print()
print('Fuel: ' + str(gas))
print('Accomodation: ' + str(accomodation))
print('Food: ' + str(food))
print()
print('Remaining Balance: ' + str(remaining))
