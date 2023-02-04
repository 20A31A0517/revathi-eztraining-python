q1="""Which country won FIFA World Cup 2022?
a)Argentina
b)England
c)Morocco
d)France
"""
q2="""Who is the best singer in India?
a)Arjit Singh
b)Shreya Ghoshal
c)Sonu Nigam
d)A.R.Rahman
"""
q3="""Which is the No 1 grossing movie in India?
a)RRR
b)Baahubali 2: The Conclusion
c)Dangal
d)K.G.F: Chapter 2
"""
q4="""Who is the founder of 
a)Mike Krieger
b)Kevin Systrom
c)Adam Mossari
d)Binny Sanchal
"""
q5="""In which year salt satyagraha took place?
a)1937
b)1930
c)1935
d)1939
"""
questions={q1:'a',q2:'d',q3:'c',q4:'b',q5:'b'}
name=input("Enter your name:")
print("Hello",name,"Welcome to the quiz!")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this question?(yes/no)")
    if flag1=="yes":
        continue
    ans=input("Enter the answer:")
    if ans==questions[i]:
        score+=1
        print("Your current score is ",score)
    else:
        score-=1
        print("Your current score is ",score)
    flag2=input("Do you want to quit the quiz?(yes/no)")
    if flag2=="yes":
        break
print("Your total score is ",score)


























              
