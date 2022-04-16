# printing empty dictionary

# dict= {}
# print(dict)

# creating a nested dictionary
# Dict = {1:'Geeks', 2: 'For', 
#        3:{'A' : 'Welcome', 'B' : 'To' , 'C': 'Geeks' }}  

# print(Dict) 


# How  to add elements in dictionary



Dict={}
Dict[0] = 'myname'
Dict[1] = 'is'
Dict[2] = 'krishnkant singh'

print(Dict)

# Adding set of values  to a single key
Dict['Value_set'] = 2,3,4
print(Dict)

# updating existing key values
Dict[2] = 'welcome'
print(Dict)

# adding nested key values to dictionary
Dict[5] = {'Nested': {'1' : 'Life', '2' : 'Geeks'}}
print(Dict)


# Accessing elements from a Dictionary using key values
print(Dict[1])

# Another method using get method in dictionary
print(Dict.get(1))

# Accessing an element of a nested dictionary
# In order to access the value of any key in the nested dictionary, use indexing [] syntax.

Dict3 = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}
print(Dict3['Dict1'][1])

# Removing element from dictionary
# using del keyword

Dict4 = { 5:'Welcome', 6: 'To' , 7:'Geeks',
         'A' :{1:'Geeks', 2: 'For', 3: 'Geeks'},
         'B' :{1:'Geeks', 2: 'Life'}}




# deleting a key values
del Dict4[6]
print(Dict4)


del Dict4['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict4)


# Using pop() method
# Pop() method is used to return and delete the value of the key specified.