#Bulls&Cows
import random
z=int(input("Enter 0 for 2 player, or 1 for single player : "))
if z==1:
    turn=0
    num=""
    a=[1,2,3,4,5,6,7,8,9,0]
    for i in range(1,5):
        x=random.choice(a)
        a.remove(x)
        num=num+str(x)
    while 1==1:
        turn+=1
        while 2==2:
            g=input("Enter your guess : ")
            if len(g)==4:
                break
        bulls=0
        cows=0
        for t in range(0,4):
            if g[t]==num[t]:
                bulls+=1
            elif g[t] in num:
                cows+=1
        print("Bulls=",bulls,end=" & ")
        print("Cows=",cows)
        if bulls==4:
            print("you win bruh")
            print("The number was: ",num)
            print("You took ",turn," number of turns")
            break
elif z==0:
    p1=0
    p2=0
    p1c=input("Player1 enter your 4-digit code : ")
    turn=0
    while 1==1:
        turn+=1
        while 3==3:
            p2g=input("Player2 enter your guess : ")
            if len(p2g)==4:
                break
        b1=0
        c1=0
        for w in range(0,4):
            if p2g[w]==p1c[w]:
                b1+=1
            elif p2g[w] in p1c:
                c1+=1
        print("Bulls=",b1,end=" & ")
        print("Cows=",c1)
        if b1==4:
            p2=turn
            print("~~~Right, the code was ",p1c)
            print("~~~You took ",turn," number of turns")
            break
    print("NOW")
    p2c=input("Player2 enter your 4-digit code : ")
    turn1=0
    while 9==9:
        turn1+=1
        while 7==7:
            p1g=input("Player1 enter your guess : ")
            if len(p1g)==4:
                break
        bb=0
        cc=0
        for h in range(0,4):
            if p1g[h]==p2c[h]:
                bb+=1
            elif p1g[h] in p2c:
                cc+=1
        print("Bulls=",bb,end=" & ")
        print("Cows=",cc)
        if bb==4:
            p1=turn1
            print("~~~Right, the code was ",p2c)
            print("~~~You took ",turn1," number of turns")
            break
    if p1>p2:
        print("Player2 wins")
    elif p1<p2:
        print("Player1 wins")
    else:
        print("The game ends in draw")