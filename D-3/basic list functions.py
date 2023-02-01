#basic indexing functions using lists

L=[1,3,62.4,'day',37]
print(L)
print(L[2])
print(L[2:3])
print(L[2:5])
print(L[0:])
print(L[:5])
print(L[-1])
print(L[::-1])

#basic list functions
#-->append,extend,insert,remove,pop,clear,index,count,reverse,sort,copy,len
l=[1,3,38.92,190,3,836,54,27]
l1=l.copy()
print(l)
l.append(4)
print(l)
l.extend([5,6])
print(l)
l.insert(1,34)
print(l)
l.remove(34)
print(l)
l.pop(3)
print(l)
print(l.index(1))
print(l.count(3))
l.sort()
print(l)
l.reverse()
print(l)
print(len(l))
l.clear()
print(l)
print(len(l))
print(l1)
