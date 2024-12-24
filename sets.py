# Immutable and no duplicate entries
# Not used as much as list or dictonary, also uses {} brackets to create but the diff is in dictonary we have key:value pair, in sets we just have value\
# Also it is unordered
from loguru import logger

set_variable = {1,2,7,8,4,12}

# print(set_variable)
#Notice it is unordred, and no duplicate enteries

# for number in set_variable:
#     print(number)

# new_set = {2,4,6,5,15}

# print(set_variable.union(new_set))

# print(set_variable.intersection(new_set))

# print(set_variable.isdisjoint(new_set))

#Assignment 1, Find missing values in l2

# List_1 = [1,2,3,4,5,6,7,8]
# list_2 = [4,5,6,7,8]

# t1 = set(List_1)
# t2 = set(list_2)

# print(t1.difference(t2))

#Assignment 2, Find common values from 3 arrays

arr1 = [1,5,10,20,40,80]

arr2 = [6,7,80,20,100]

arr3 = [3,4,15,20,30,70,80,120]


final_output = []

for number in arr1:
    if number in arr2 and arr3:
        final_output.append(number)
    else:
        continue
print(final_output)