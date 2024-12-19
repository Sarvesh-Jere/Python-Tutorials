a=5
print(a>5)
print(a<=5)
#Whenever we use conditionl operator that is >,< etc we get answer in true or false
# In if else only the True condition runs 
# if True:
#print()
#else:
#print()

from loguru import logger
import math


length_of_land = 100
brick_cost_per_piece = 10.5
labour = "Sarvesh"
Home = True


length_of_land = int(input("Enter length of Land: "))

if length_of_land < 100:
    logger.info(f"Length of your land is not sufficent")
    if length_of_land >80:
        logger.info(f"Length of land is Just short")
    else:
        logger.info("Length should be increased just a little")
elif length_of_land > 500:
    logger.info(f"Can build more buildings")
else:
    logger.info(f"Share more details with us")

# It runs until it gets true condition

#ODD and EVEN sum

number = int(input("Enter a number"))

if number % 2 == 0:
    logger.info("It is an even number")
else:
    logger.info("It is an odd number")
    
