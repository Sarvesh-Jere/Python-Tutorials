# very important, function is used 
#basic syntax
# def(keyword) cost_of_area(function_name)(length,breadth,cost)(argument1,argument2,argument3): - They are basiclly variable names
# The required fromulas
# 
# return cost_for_fencing( the required output value)
# 
# Now to call the function - 
#  var_name = cost_for_fencing(100,70,17)

#note - dont loope more than 3 or 4 functions inside 1

def cost_of_area(length, breadth, cost):
    area = length * breadth
    area_cost = cost * area
    return area_cost

Total_cost = cost_of_area(10, 7, 2)
print(Total_cost)
