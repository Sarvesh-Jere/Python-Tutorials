from loguru import logger
# List comprehension alwasy returns a list
# First lets do this by for loop

new_list = []

old_list = [1,2,3,4,5,6,7,8,9]

for numbers in old_list:
    if numbers % 2 == 0:
        new_list.append(numbers)

logger.info(new_list)

# Now using list comprehension, Note - list comprehension is not used in complex examples.
# First just if it had if statement

new_list = [numbers for numbers in old_list if numbers %2 ==0]

logger.info(new_list)

# Now to see for if else both



ew_list = []

old_list = [1,2,3,4,5,6,7,8,9]

new_list1 = [["Even" if i%2==0 else "Odd" for i in range(1,11)]]

print(new_list1)