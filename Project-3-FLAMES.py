n1=input("Enter the name1:").lower()
n2=input("Enter the name2:").lower()
n1=n1.replace(" ","")
n2=n2.replace(" ","")
print(n1)
print(n2)
for i in n1:
    for j in n2:
        if i==j:
            n1=n1.replace(i,"",1)
            n2=n2.replace(j,"",1)
            break
count=len(n1+n2)
print(count)
if count>0:
    l=['Friends','Lovers','Affectionate','Marriage','Enemies','Siblings']
    while len(l)>1:
        c=count%len(l)
        s_index=c-1
#slicing
        if s_index>=0:
            left=l[:s_index]
            right=l[s_index+1:]
            l=right+left
        else:
            l=l[:len(l)-1]
    print("Relationship:",l[0])
else:
    print("Enter differnt names:")
                
