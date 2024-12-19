# Used in NoSQl database and to hit any API
# Also called as JSON files, Stored in KV pairs. 

from loguru import logger

labour_dict = {"Mahesh":400,"Mithesh":300}

#logger.info(labour_dict)

#update the dict, or add value to dict 

#labour_dict["Ramesh"]=1000

#logger.info(labour_dict)

# Now in real life we use iterate , we dont keep creating and updating dict

#logger.info(labour_dict.keys())
#logger.info(labour_dict.values())
#logger.info(labour_dict.items())

# Now to iterate, use for loop but by default the for loop gives the key one by one

#for abc in labour_dict:
    #print(abc)

# Now to get both key and value, we have to add , value and to access value we use labour_dict["key name"]

#for abc in labour_dict:
   # print(abc, labour_dict[abc])

#Now another method

#for key,value in labour_dict.items():
    #print(key,value)

# Assignment total cost of 50 days 
labour_dict = {"Mahesh":400,"Mithesh":300}

labour_days = {"Mahesh":47,"Mithesh":30}

for cost in labour_dict:
    if cost in labour_days:
        print(labour_days[cost]*labour_dict[cost])
