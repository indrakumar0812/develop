# Python3 program to swap elements 
# at given positions 

# Swap function 
def swapPositions(list, pos1, pos2): 
	
	# popping both the elements from list 
	first_ele = list.pop(pos1)
	print(first_ele)
	second_ele = list.pop(pos2-1)
	print(second_ele)
	print(list)
	
	# inserting in each others positions 
	list.insert(pos1, second_ele) 
	list.insert(pos2, first_ele) 
	
	return list

# Driver function 
List = [23, 65, 19, 90,50,40] 
pos1, pos2 =2,4

print(swapPositions(List, pos1-1, pos2-1)) 

