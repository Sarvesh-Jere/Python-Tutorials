from loguru import logger

labour_names = ["Sarvesh","Suyash","Prathamesh","Aditya"]

logger.info(f"The first name in my list is {labour_names[0]}")
# We used positive indexing 
# Remember all the data is stored in Ram before using

# We can use append to add values to the list 

labour_names.append("Raj")

logger.info(labour_names)

#But we can only add 1 at a time and thats not enough 
#Mthod 2 - Use extend 

add_labour = ["Gaur","Khush"]

labour_names.extend(add_labour)
logger.info(labour_names)

#But it only adds at the end

#method-3 Use insert

labour_names.insert(0,"Ram")
logger.info(labour_names)

#Multidimesnional List

labour_withwage = [["sarvesh",500],["rajesh",600]]
logger.info(labour_withwage[0][1])