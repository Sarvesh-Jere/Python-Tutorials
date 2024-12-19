from loguru import logger

print("Programming")

labour_name = ["sarvesh","suyash","aditya","prathamesh"]

#Method 1 to access for loop
for name in labour_name:
    logger.info(name)

# method 2 using range 

for i in range(5):
    logger.info(i)

for i in range(len(labour_name)):
    logger.info(f"labour {i+1} name is {labour_name[i]}")