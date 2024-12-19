from loguru import logger

labour_cost = {"manish":500, "sarvesh":600, "Prathamesh":750, "aditya":850}

# Dictonary comprehension, using get method. .get(pass key) to get value

print(labour_cost.get("sarvesh"))

# Update method to update value of key, not used much nowadays

labour_cost.update({"manish":750})

print(labour_cost)

#Another method is suing ** stars to merge the dictonaries 

labour_cost = {"manish":500, "sarvesh":600, "Prathamesh":750, "aditya":850}

labour_new = {"manish":500, "sarvesh":600, "Guransh":980}

final_dict = {**labour_cost,**labour_new}

print(final_dict)

# Pop method rarely used

(labour_cost.pop("manish"))

print(labour_cost)

# Dictonary comprehension, similar to list comprehension, is used more than all the things above
# Syntax for the same - new_list = {Output if condition else output for loop}

labour_cost = {"manish":500, "sarvesh":600, "Prathamesh":750, "aditya":850}

labour_cost = {key:labour_cost[key] + 100 for key in labour_cost}

labour_cost = {key:labour_cost[key]+100 if key!= "aditya" else key for key in labour_cost}



print(labour_cost)

# In method, important in interview, where is it faster - Dictonary or List? Study Time space complexity 

name = "Manish"

letter = {}

for name in letter:
    if char in letter:
        letter[char] +=1
    else:
        letter[char] = 1

        print(name)

