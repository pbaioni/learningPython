# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed data types
my_list = [1, "Hello", 3.4]

print(my_list)

my_list = ['p', 'r', 'o', 'b', 'e', 's']

#printing first item
print(my_list[1]) # r

#printing last item
print(my_list[-1]) # s

# elements 3rd to 5th
print(my_list[2:5])

# elements from 4th last to beginning
print(my_list[:-5])

# elements from 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

# delete one item in position 2
del my_list[2]
print(my_list)

# delete multiple items, from indexes 1 to 3 (two items)
del my_list[1:3]
print(my_list)

# delete entire list
del my_list

# new numerical list
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  
print(odd)

#append an element
odd.append(8)
print(odd)

#extend the list
odd.extend([9, 11, 13])
print(odd)

#insert the number '99' in position 1
odd.insert(1,99)
print(odd)

#insert elements starting from position 2
odd[2:2] = [0, 0]
print(odd)

#remove the last '0' found in the list
odd.remove(0)
print(odd)

#remove and return the element at index 4
print(odd.pop(4))

#reversing the list
odd.reverse()
print(odd)