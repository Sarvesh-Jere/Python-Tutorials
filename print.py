#print("Programming")
#variable

length = 100
print(length)
print(id(length))

breadth = 100
print(length, breadth)
print(id(length),id(breadth))
# Note that both id are same cause the value are same cause what the id basically means is the location on the ram where the object/data is being stored which will 
# be same in case of same values

# Data Types

length_of_land = 100
brick_cost_per_piece = 10.5
labour = "Sarvesh"
Home = True

print(length_of_land,brick_cost_per_piece,labour,Home)


if length_of_land == int(100):
    length_of_land == 200
else:
    length_of_land == 300



print(length_of_land)
# This is how you write an ewxplainable code, can use both single and double quotes 
print("length of land is",length_of_land)

# For new line we use \n in print statement 

print("We are testing the new line \nfeature")

# Can also use triple quotes for multi line 

print (''' Testing mult line 
Testing multi line ''')

#using both single quotes and double quotes to highlight 4bhk
print("my home is of '4 bhk' ")
#Can also use backward slash whoich skips the next character, these are all escape sequenbces by the way

print("my home is of \"4 bhk\" ")

#string fromating 
# 1) f string, use {} to call the variable which you want to call, also use f before inside print

print(f"The cost per unit is {brick_cost_per_piece}")

#2) The second method is .format. It is used as follows

print("The cost per unit of brick is {}".format(brick_cost_per_piece))

#Logging in Python - Used to see the line, dat etc of code basically the log files of python 

import logging

# Configure the logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info(f"The cost per unit is {brick_cost_per_piece}")

# Using library loguru, first intall loguru in terminal below then import it here 


from loguru import logger 

logger.info(f"The cost per unit is {brick_cost_per_piece}")
