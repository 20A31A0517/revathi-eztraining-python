#check if given number is Neon number or not
n=int(input("enter a number:"))
square=n*n
sum=0
while square!=0:
    digit=square%10
    sum+=digit
    square=square//10
if sum==n:
    print("Given number ",n," is a neon number")
else:
    print("Given number ",n," is not a neon number")
