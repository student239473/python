
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

def kmh_to_ms(speed_kmh):
    speed_ms = speed_kmh * 1000 / 3600
    return speed_ms

speed_kmh = float(input("Enter speed in km/h: "))

speed_ms = kmh_to_ms(speed_kmh)
print(f"The speed in m/s is: {speed_ms:.2f} m/s")

#############################################################################
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print(f"The length of the diagonal is: {diagonal:.2f}")
#################################################################################
import math
def distance_to_horizon(height):
    distance = 3.57 * math.sqrt(height)
    return distance
height = float(input("Enter the height above the ground in meters: "))
distance = distance_to_horizon(height)
print(f"The distance to the horizon is: {distance:.2f} kilometers")
beach_height = 1.7
beach_distance = distance_to_horizon(beach_height)
print(f"\nAt the beach (height {beach_height} m), the horizon is: {beach_distance:.2f} km away")
hotel_height = 20
hotel_distance = distance_to_horizon(hotel_height)
print(f"From a hotel window at 20 m, the horizon is: {hotel_distance:.2f} km away")
##############################################################################################

total_population = 8000000000  
northern_population = 7200000000  
southern_population = total_population - northern_population
northern_percentage = (northern_population / total_population) * 100
southern_percentage = (southern_population / total_population) * 100
print(f"Population in the Northern Hemisphere: {northern_population} people")
print(f"Percentage in the Northern Hemisphere: {northern_percentage:.2f}%")
print(f"Population in the Southern Hemisphere: {southern_population} people")
print(f"Percentage in the Southern Hemisphere: {southern_percentage:.2f}%")
###############################################################################################
###
# A program that calculates and prints
# the average grade of a student
#
mat = 5
Art = 4
muzic = 5
history = 3
average = mat + Art - muzic + history / 4
print("Average grade is", average)

####################################################################################################

name = "Adam"
age = 20  
height = 175 

print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height} cm.")
print(f"In 6 years I will be {age + 6} years old.")
