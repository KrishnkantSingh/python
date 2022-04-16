# dictionary - collection of key pair of values
'''features - 1) ordered
           2) mutuable
           3) no duplicacy '''

from turtle import update


d = {1 : 'krishnkant', 2: 'jaipreet' , 3: 'piyush', 4: 'axsh',}
print(d[1])

for i in range(1,3):
    print(d[i])



m = d.get(2)
print(m)

print(d.keys())
print(d.values())
d.update({1:"r"})




