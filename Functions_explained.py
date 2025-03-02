Sarvesh_expense = [2100,1400,700]
Skbidi_expense = [210,140,70]

# Here we  hvae 2 list and to find the total expense of both list we will need to use for loop for both,

total = 0
for number in Sarvesh_expense:
    total = number + total
print(total)


total = 0
for number in Skbidi_expense:
    total = number + total
print(total)

# Now this we are able to do cause there are just 2 lists, now imagine for 100s of list this wont be possible, thats why we need functions

# Basically function is an encapsulation of code that can be called to run whenever required 

# now with dunctions 

def calculte_total(exp):
    total = 0
    for number in exp:
        total = number + total
    return total

total_sarvesh = calculte_total(Sarvesh_expense)
total_Skibdi = calculte_total(Skbidi_expense)

print(total_sarvesh)
