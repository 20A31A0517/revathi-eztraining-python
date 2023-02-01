#list comprehensions method 1-->can create list using existing list
l=["hyderabad","vizag","chennai","vijayawada"]
city=[]
for n in l:
    if "v" in n:
        city.append(n)
print(city)

#list comprehensions method 2-->can create list using for loops
l1=[2**x for x in range(2,10)]
print(l1)
l2=[a for a in range(100,201,10)]
print(l2)
l3=[1,2,3,4,5,6,7]
print(l3)
l4=[i for i in l3 if(i<5)]
print(l4)
