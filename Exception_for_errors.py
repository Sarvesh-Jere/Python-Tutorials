# Exception is the error message we pass after getting some error in programming

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


# Chatgpt defination - Raising an exception in Python means interrupting the normal flow of the program to signal that an error or unusual condition has occurred. 
# You can explicitly raise exceptions using the raise statement.

# we use try and except to continue the flow of program even though there is some error, therefore an exception as shown below.
# We mostly give specific error for example type error and then give exception error e in the last.


def total_amount(discount=0.5, **kwargs):
    try:
        result = 0
        for key, amount in kwargs.items():
            result += amount  # Sum values of the keyword arguments

        amount_after_discount = result - (result * discount)  # Apply discount
        return amount_after_discount
    except TypeError:
        print("Type error, Please give an integer")
    except Exception as e:
        print("Cannot proceed further")
        raise e

# Example usage: Pass named arguments for amounts
final_paid = total_amount(a=100, b=200, c=300, d=400, e='500', discount=0.5)

# Log the final result
logger.info(f"Final amount paid: {final_paid}")

# Now in the same example if we add raise e, then the stop the code flow give the error message and use exception as given by the chatgpt defination. 
