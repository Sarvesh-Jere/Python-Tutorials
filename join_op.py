from loguru import logger

# The syntax of join is result = " "(this isthe seperator).join(iterable)-(this can be set,tuple,dictonary or list but must be a string)

# list and dictonary are used a lot

lst = ['1','10','7','9']

result = " ".join(lst)

print(result)

#example of real use case
dept_info = [
    {"state": "Maharashtra", "dept": "IT"},
    {"state": "Gujrat", "dept": "Marketing"}
]

final = []

for condition in dept_info:
    for Key,Value in condition.items():
        final.append(f"{Key } = { Value}")

print(final)


result = " OR ".join(final)

print(result)