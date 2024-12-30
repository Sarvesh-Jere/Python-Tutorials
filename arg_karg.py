# arg is used in a function when we want to pass more values in the function in which we cannot use positional arguments
# While using arg the values passed gets converted into a touple 

from loguru import logger

def total_amount(*args, discount):
    result = 0
    for amount in args:
        result += amount  

    amount_after_discount = result - (result * discount)  
    return amount_after_discount

# Correct function name and usage
final_paid = total_amount(100, 200, 300, 400, 500, discount=0.5)

# Log the final result
logger.info(f"Final amount paid: {final_paid}")

# Now for default argument we pass the discount before so it takes that discount if no value is found


def total_amount(*args, discount = 0.5):
    result = 0
    for amount in args:
        result += amount  

    amount_after_discount = result - (result * discount)  
    return amount_after_discount

# Correct function name and usage
final_paid = total_amount(100, 200, 300, 400, 500)

# Log the final result
logger.info(f"Final amount paid: {final_paid}")

# Now for keyword arguments we use kwargs, kwargs converts it into dictionary and not touple and therefore is useful when we want to iterate in key,value pairs

from loguru import logger

def total_amount(discount=0.5, **kwargs):
    result = 0
    for key, amount in kwargs.items():
        result += amount  # Sum values of the keyword arguments

    amount_after_discount = result - (result * discount)  # Apply discount
    return amount_after_discount

# Example usage: Pass named arguments for amounts
final_paid = total_amount(a=100, b=200, c=300, d=400, e=500, discount=0.5)

# Log the final result
logger.info(f"Final amount paid: {final_paid}")
