krishnkant_singh=["apple", "banana", "cherry","watermelon", "oranges"]
print(krishnkant_singh)

# we will perform diffrent methods on list
krishnkant_singh.append("orange")    #The append() method appends an element to the end of the list.
krishnkant_singh.clear()             #Remove all elements from the fruits list:
x = krishnkant_singh.copy()          #The copy() method returns a copy of the specified list.
print(x)
y = krishnkant_singh.count("oranges") #Return the number of times the value "oranges" appears in the fruits list:
print(y)
#The extend() method adds the specified list elements (or any iterable) to the end of the current list.
cars = ['Ford', 'BMW', 'Volvo']
krishnkant_singh.extend(cars)

x = krishnkant_singh.index("oranges")      #The index() method returns the position at the first occurrence of the specified value.
krishnkant_singh.insert(1, "game")        #The insert() method inserts the specified value at the specified position.
krishnkant_singh.pop(1)                   #The pop() method removes the element at the specified position.
krishnkant_singh.remove("banana")         #The remove() method removes the first occurrence of the element with the specified value.
krishnkant_singh.reverse()                #The reverse() method reverses the sorting order of the elements.
# krishnkant_singh.sort()                   #The sort() method sorts the list ascending by default.