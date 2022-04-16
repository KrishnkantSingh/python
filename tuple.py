books = ['id1', 'id2', 'id3',]

for i in range(0, len(books)):
    print(books[i])


for i in books:
    print(i)



# Accessing Tuple
# with Indexing
Tuple1 = tuple("krishnkant")
print("\nFirst element of Tuple: ")
print(Tuple1[0])



Tuple1 = ("krishnkant",  "singh")


a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)
