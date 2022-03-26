A,B =map(int, input().split())
if A !=0 :
    if B-45>=0:
        print('%d %d '%(A,B-45))
    elif B-45<0:
        print('%d %d' %(A-1,(B-45)+60))
else :
    if B-45>=0:
        print('%d %d '%(A,B-45))
    elif B-45<0:
        print('%d %d'%((A+24)-1,(B-45)+60))
