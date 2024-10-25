
###
# BMI Calculator
#
height = input('Enter your height in cm: ')
weight = input('Enter your weight in kg: ')
height = int(height)
weight = int(weight)
bmi = weight / (height/100)**2
bmi = round(bmi,2)
print('Your BMI is', bmi)
print('Check on the Internet if your BMI is ok!!')


###################################################

import random
print("Dice rolling simulator")
for i in range(5):
    dice_roll = random.randint(1,6)
    print(dice_roll, end=" ")

#################################################

wartoscp = 1

print(type(wartoscp))

########################################################
company = "ABC Data" # Name - Company    Value- ABC      Type - String #
phone = "555-123-009" # Name- phone     Value 555-123-009     Type -String #
employees = 25 #Name employees     Value  25   Type INT#
remote_work = True #Name remote_work     Value True     Type  bool#
big_company = employees > 100 #Name  big_company     Value NO    Type bool#
income = 4500000 #Name income      Value 4500000    Type int#
income_per_person = income / employees #Name  income_per_person     Value 180000    Type INT#


###############################################################

###
# A program that calculates the sum of two numbers.
# Modify the program to calculate the sum of three numbers.
#
number3 = 21
number1 = 71
number2 = 14
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)

######################################################################

x = 7
y = 34
Z =  0
print("Before swapping: x=", x, "y=", y)

Z = y
y= x
x = Z
print("After swapping: x=", x, "y=", y)

###########################################################################


