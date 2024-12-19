from loguru import logger

print("Programming")

for i in range(5):
    print("*")

# Now to do this for a * shaped right angled triangle

for i in range(5):
    print((i+1) * "* ")

#Print all even numbers using for loop

for number in range(101):
    if number % 2 == 0:
       print(number)

for i in range(4, -1, -1):
    print((i+1) * "* ")