#1)create a list with 10 items and print the elements one by one.

L=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(L)):
    print(L[i])
#method-2 ->using membership operator
for j in L:
    print(j)

#2)create a list with 5 float numbers and find out sum & average.

l=[1.23,3.45,55.2,78.34,8.9]
sum=0
for j in l:
    sum+=j
print(sum)
average=sum/5
print(average)

#3)after creating a list with 6 elements from user and print even numbers.

l1=[1,2,3,4,5,6]
for i in l1:
    if(i%2==0):
        print(i)

#4)take a list from user input and print even numbers.

size=int(input("size:"))
list=[]
print("elements:")
for i in range(size):
    ele=int(input())
    list.append(ele)
print(list)
print("even elements:")
for i in list:
    if(i%2==0):
        print(i)

#5)take a list from user input and print product if the product is less than 750 else print sum.

size=int(input("size:"))
lst=[]
sum=0
prod=1
print("elements:")
for i in range(size):
    ele=int(input())
    lst.append(ele)
print(lst)
for i in lst:
    prod=prod*i
    sum=sum+i
if prod<=750:
    print("product of the list is ",prod)
else:
    print("sum of the list is ",sum)

#method -2 --> without taking size
list1=list(map(int,input("Elements:").strip().split()))
sum=0
prod=1
print(list1)
for i in list1:
    prod=prod*i
    sum=sum+i
if prod<=750:
    print("product of the list is ",prod)
else:
    print("sum of the list is ",sum)
