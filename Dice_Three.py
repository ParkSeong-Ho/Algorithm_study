DICE1,DICE2,DICE3 =map(int,input().split())
same=0
A=0
money=0
value=0
if DICE1==DICE2:
    same+=1
if DICE1==DICE3:
    same+=1
if DICE2 == DICE3:
    same+=1
if same ==3:
   money=10000+DICE1*1000
elif same == 1:
    if DICE1 == DICE2 and DICE1 !=DICE3:
        A=DICE1
    elif DICE1 == DICE3 and DICE2 !=DICE3:
        A=DICE1
    elif DICE2 == DICE3 and DICE1 !=DICE2:
        A=DICE2
    money =1000+A*100
elif same==0:
    list=[DICE1,DICE2,DICE3]
    max1=list[0]
    for i in list:
        if i>max1:
            max1=i
    money=max1*100
print(money)
