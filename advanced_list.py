from loguru import logger

labour_names = ["Sarvesh","Suyash","Prathamesh","Aditya"]

new_labour = ["rajesh", "Mithesh"]
# Adding two list is a better method than using .extend
labour_names = labour_names + new_labour
print(labour_names)

#Accessing values in list using :

print(labour_names[1:4])

#how to reverse a list 

print(labour_names[::-1])
# Count number of elements using length method 

print(len(labour_names))

#Use insert method like .insert(position, value)
labour_names.insert(3, "Ashutosh")
logger.info(labour_names)

#Pop is used to delete elements, mostly used in stack and queue, Also pop returns the deleted value 

print(labour_names.pop())

# Use remove to remove duplicate values

labour_names = ["Sarvesh","Suyash","Prathamesh","Aditya","Aditya"]

labour_names.remove("Aditya")
print(labour_names)

# Change values in a list
labour_names = ["Sarvesh","Suyash","Prathamesh","Aditya","Aditya"]

labour_names[0] = "Vedang"

print(labour_names)

# Split method , .split("")

api_endpoint = "https://portal.azure.com/VMINSTANCE/test-vm/subs_id/aexy-234-mns/getCredential"

new_api = api_endpoint.split("/")

print(new_api[-1])
