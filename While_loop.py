from loguru import logger
import time

labour_name = ["Sarvesh","Suyash","Aditya","Prathamesh"]

# This is the syntax for while loop, first define the variable. Next write while condition and then manually specify how you want the loop to funcation after print.abs

name_iter = 0
while(name_iter<len(labour_name)):
    logger.info(labour_name[name_iter])
    time.sleep(5)
    #Use to cause a delay -  time.sleep()
    name_iter = name_iter +1
# Very important to close the loop with the name_iter =+1 or will print infinetly 
 


