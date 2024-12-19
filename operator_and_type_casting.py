from loguru import logger
import math


length_of_land = 100
brick_cost_per_piece = 10.5
labour = "Sarvesh"
Home = True

#Calcullate the total area of the land
total_area_o_land = length_of_land*brick_cost_per_piece

logger.info(f"The total area of the land is {total_area_o_land} sq ft")

perimeter_of_land = 2 * (length_of_land + brick_cost_per_piece)

logger.info(f"The perimter of the land is {perimeter_of_land}")
# Modulo operator, used tro give reminder in division, Used when armstrong number code

print(15%6)
#gives 3

#Floor division 1)
print(15//6)

#2
print(math.floor(15/6))

#Ceiling Division 
print(math.ceil(15/6))

# Type Casting, change data type according to need 
a = "15"
b = 20

print(a+str(b))

#Take input from the user 
length_of_your = float(input("Enter ur length"))

breadth_of_your = float(input("Enter ur breadth"))

area_of_your_home = length_of_your * breadth_of_your

logger.info(f"Total Land {area_of_your_home}")

#Use abs() which is absolute to remove decimal points and remove negative quotation if user gives negative number  by mistake