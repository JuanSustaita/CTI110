# This program is to help other people budget properly while traveling
# Date: Feb 27, 2023
# CTI-110 P2HW1 - Travel Expense
# Juan Sustaita
#
print('This program calculates and displays travel expenses')
print()

budget = int(input('Enter Budget: '))
print()
destination = input('Enter your travel destination: ')
print()
gas = int(input('How much do you think you will spend on gas? '))
print()
accomodation = int(input('Approximately, how much will you need for accomodation/hotel? '))
print()
food = int(input('Last, how much do you need for food? '))
print()
remaining = budget - gas - accomodation - food
print("------------Travel Expenses------------")
print(f"{'Location:' : <20}", f"{ destination : <20}") 
print(f"{'Initial Budget:' : <20}", f" { '$' + str(float(budget)) : <20}")
print(f"{'Fuel:' : <20}", f"{'$' + str(float(gas)) : <20}")
print(f"{'Accomodation:' : <20}", f" {'$' + str(float(accomodation)) : <20}")
print(f"{'Food:' : <20}", f"{'$' + str(float(food)) : <20}")
print("---------------------------------------")
print()
print(f"{'Remaining Balance:' : <20}", f"{'$' + str(float(remaining)): <20}")
