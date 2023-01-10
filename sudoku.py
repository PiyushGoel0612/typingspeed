import random as rd
d=1
b111=[1,2,3,4,5,6,7,8,9]
b211=[1,2,3,4,5,6,7,8,9]
b311=[1,2,3,4,5,6,7,8,9]
b112=[1,2,3,4,5,6,7,8,9]
b212=[1,2,3,4,5,6,7,8,9]
b312=[1,2,3,4,5,6,7,8,9]
b113=[1,2,3,4,5,6,7,8,9]
b213=[1,2,3,4,5,6,7,8,9]
b313=[1,2,3,4,5,6,7,8,9]
while d in range(1,4):
    a1=[1,2,3,4,5,6,7,8,9]
    a2=[1,2,3,4,5,6,7,8,9]
    a3=[1,2,3,4,5,6,7,8,9]
    c1=[1,2,3,4,5,6,7,8,9]
    c2=[1,2,3,4,5,6,7,8,9]
    c3=[1,2,3,4,5,6,7,8,9]
    c=1
    while c in range(1,8):
        if c%2!=0:
            a=1
            while a in range(1,4):
                b=1
                while b in range(1,8):
                    if b%2==0:
                        print("~",end=" ")
                    else:
                        print("+",end=" ")
                    b=b+1
                print("  ",end="")
                a=a+1
            print("")
        else:
            a=1
            while a in range(1,4):
                b=1
                while b in range(1,8):
                    if b%2==0:
                        k=[1,2]
                        o=rd.choice(k)
                        if o==1:
                            print(" ",end=" ")
                        else:
                            for i in range(1,4):
                                if b==2 and a==1 and c==4 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b111)
                                        w=rd.choice(a1)
                                        e=rd.choice(c1)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b111.remove(q)
                                            a1.remove(q)
                                            c1.remove(q)
                                            break
                                if b==4 and a==1 and c==4 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b112)
                                        w=rd.choice(a1)
                                        e=rd.choice(c1)
                                        if q==w and w==e:
                                            print(q,end=" ")                                   
                                            a1.remove(q)
                                            b112.remove(q)                                       
                                            c1.remove(q)
                                            break
                                if b==6 and a==1 and c==4 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b113)
                                        w=rd.choice(a1)
                                        e=rd.choice(c1)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b113.remove(q)
                                            a1.remove(q)
                                            c1.remove(q)
                                            break
                                if b==2 and a==2 and c==4 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b211)
                                        w=rd.choice(a2)
                                        e=rd.choice(c1)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b211.remove(q)
                                            a2.remove(q)
                                            c1.remove(q)
                                            break
                                if b==4 and a==2 and c==4 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b212)
                                        w=rd.choice(a2)
                                        e=rd.choice(c1)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b212.remove(q)
                                            a2.remove(q)
                                            c1.remove(q)
                                            break
                                if b==6 and a==2 and c==4 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b213)
                                        w=rd.choice(a2)
                                        e=rd.choice(c1)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b213.remove(q)
                                            a2.remove(q)
                                            c1.remove(q)
                                            break
                                if b==2 and a==3 and c==4 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b311)
                                        w=rd.choice(a3)
                                        e=rd.choice(c1)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b311.remove(q)
                                            a3.remove(q)
                                            c1.remove(q)
                                            break
                                if b==4 and a==3 and c==4 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b312)
                                        w=rd.choice(a3)
                                        e=rd.choice(c1)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b312.remove(q)
                                            a3.remove(q)
                                            c1.remove(q)
                                            break
                                if b==6 and a==3 and c==4 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b313)
                                        w=rd.choice(a3)
                                        e=rd.choice(c1)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b313.remove(q)
                                            a3.remove(q)
                                            c1.remove(q)
                                            break
                                if b==2 and a==1 and c==2 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b111)
                                        w=rd.choice(a1)
                                        e=rd.choice(c2)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b111.remove(q)
                                            a1.remove(q)
                                            c2.remove(q)
                                            break
                                if b==4 and a==1 and c==2 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b112)
                                        w=rd.choice(a1)
                                        e=rd.choice(c2)
                                        if q==w and w==e:
                                            print(q,end=" ")                                   
                                            a1.remove(q)
                                            b112.remove(q)                                       
                                            c2.remove(q)
                                            break
                                if b==6 and a==1 and c==2 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b113)
                                        w=rd.choice(a1)
                                        e=rd.choice(c2)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b113.remove(q)
                                            a1.remove(q)
                                            c2.remove(q)
                                            break
                                if b==2 and a==2 and c==2 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b211)
                                        w=rd.choice(a2)
                                        e=rd.choice(c2)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b211.remove(q)
                                            a2.remove(q)
                                            c2.remove(q)
                                            break
                                if b==4 and a==2 and c==2 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b212)
                                        w=rd.choice(a2)
                                        e=rd.choice(c1)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b212.remove(q)
                                            a2.remove(q)
                                            c2.remove(q)
                                            break
                                if b==6 and a==2 and c==2 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b213)
                                        w=rd.choice(a2)
                                        e=rd.choice(c2)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b213.remove(q)
                                            a2.remove(q)
                                            c2.remove(q)
                                            break
                                if b==2 and a==3 and c==2 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b311)
                                        w=rd.choice(a3)
                                        e=rd.choice(c2)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b311.remove(q)
                                            a3.remove(q)
                                            c2.remove(q)
                                            break
                                if b==4 and a==3 and c==2 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b312)
                                        w=rd.choice(a3)
                                        e=rd.choice(c2)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b312.remove(q)
                                            a3.remove(q)
                                            c2.remove(q)
                                            break
                                if b==6 and a==3 and c==2 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b313)
                                        w=rd.choice(a3)
                                        e=rd.choice(c2)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b313.remove(q)
                                            a3.remove(q)
                                            c2.remove(q)
                                            break
                                if b==2 and a==1 and c==6 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b111)
                                        w=rd.choice(a1)
                                        e=rd.choice(c3)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b111.remove(q)
                                            a1.remove(q)
                                            c3.remove(q)
                                            break
                                if b==4 and a==1 and c==6 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b112)
                                        w=rd.choice(a1)
                                        e=rd.choice(c3)
                                        if q==w and w==e:
                                            print(q,end=" ")                                   
                                            a1.remove(q)
                                            b112.remove(q)                                       
                                            c3.remove(q)
                                            break
                                if b==6 and a==1 and c==6 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b113)
                                        w=rd.choice(a1)
                                        e=rd.choice(c3)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b113.remove(q)
                                            a1.remove(q)
                                            c3.remove(q)
                                            break
                                if b==2 and a==2 and c==6 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b211)
                                        w=rd.choice(a2)
                                        e=rd.choice(c3)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b211.remove(q)
                                            a2.remove(q)
                                            c3.remove(q)
                                            break
                                if b==4 and a==2 and c==6 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b212)
                                        w=rd.choice(a2)
                                        e=rd.choice(c3)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b212.remove(q)
                                            a2.remove(q)
                                            c3.remove(q)
                                            break
                                if b==6 and a==2 and c==6 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b213)
                                        w=rd.choice(a2)
                                        e=rd.choice(c3)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b213.remove(q)
                                            a2.remove(q)
                                            c3.remove(q)
                                            break
                                if b==2 and a==3 and c==6 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b311)
                                        w=rd.choice(a3)
                                        e=rd.choice(c3)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b311.remove(q)
                                            a3.remove(q)
                                            c3.remove(q)
                                            break
                                if b==4 and a==3 and c==6 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b312)
                                        w=rd.choice(a3)
                                        e=rd.choice(c3)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b312.remove(q)
                                            a3.remove(q)
                                            c3.remove(q)
                                            break
                                if b==6 and a==3 and c==6 and d==i:
                                    z=1
                                    while z==1:
                                        q=rd.choice(b313)
                                        w=rd.choice(a3)
                                        e=rd.choice(c3)
                                        if q==w and w==e:
                                            print(q,end=" ")
                                            b313.remove(q)
                                            a3.remove(q)
                                            c3.remove(q)
                                            break
                    else:
                        print("|",end=" ")
                    b=b+1
                print("  ",end="")
                a=a+1
            print("")
        c=c+1
    d=d+1
    print("  ")