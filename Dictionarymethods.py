# Dictionary Methods 
# Methods	Description
# copy()    	They copy() method returns a shallow copy of the dictionary.
# clear()  	The clear() method removes all items from the dictionary.
# pop()	    Removes and returns an element from a dictionary having the given key.
# popitem()	Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
# get()	    It is a conventional method to access a value for a key.
# dictionary_name.values()	returns a list of all the values available in a given dictionary.
# str()	     Produces a printable string representation of a dictionary.
# update()	Adds dictionary dict2’s key-values pairs to dict
# setdefault()	Set dict[key]=default if key is not already in dict
# keys()	Returns list of dictionary dict’s keys
# items()	Returns a list of dict’s (key, value) tuple pairs
# has_key()	Returns true if key in dictionary dict, false otherwise
# fromkeys()	Create a new dictionary with keys from seq and values set to value.
# type()	Returns the type of the passed variable.
# cmp()	Compares elements of both dict.


# implementation of form keys
#  It creates a new dictionary from the given sequence with the specific value.
krishnkant = {'a', 'b', 'c', 'd', 'e'}

# using fromkeys() to convert sequence to dict 
shivam = dict.fromkeys(krishnkant)
print(" the newly created dict with none values: " + str(shivam))


#using fromkeys() to convert sequence to dict
#initializing  with 1
shivam =dict.fromkeys(krishnkant, 1)

print(" the newly created dict with 1 as value : " + str(shivam))

print(" the newly created dict with 1 as value:" + str(shivam))
n
