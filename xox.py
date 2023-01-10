#TicTacToe
for z in range(1,11):    
    if z==1:
        for x in range(1,8):
            for y in range(1,8):
                if x%2!=0 and y%2!=0:
                    print("+",end=" ")
                elif x%2!=0 and y%2==0:
                    print("~",end=" ")
                elif x%2==0 and y%2!=0:
                    print("|",end=" ")
                elif x%2==0 and y%2==0:
                    print(" ",end=" ")
            print("")
    elif z==2:
        a=int(input("Player X; Enter row : "))
        b=int(input("Player X; Enter column : "))
        for x in range(1,8):
            for y in range(1,8):
                if x%2!=0 and y%2!=0:
                    print("+",end=" ")
                elif x%2!=0 and y%2==0:
                    print("~",end=" ")
                elif x%2==0 and y%2!=0:
                    print("|",end=" ")
                elif x==a*2 and y==b*2:
                    print("X",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    elif z==3:
        while 1==1:
            c=int(input("Player 0; Enter row : "))
            d=int(input("Player 0; Enter column : "))
            if c!=a or d!=b:
                break
        for x in range(1,8):
            for y in range(1,8):
                if x%2!=0 and y%2!=0:
                    print("+",end=" ")
                elif x%2!=0 and y%2==0:
                    print("~",end=" ")
                elif x%2==0 and y%2!=0:
                    print("|",end=" ")
                elif x==c*2 and y==d*2:
                    print("O",end=" ")
                elif x==a*2 and y==b*2:
                    print("X",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    elif z==4:
        while 1==1:
            e=int(input("Player X; Enter row : "))
            f=int(input("Player X; Enter column : "))
            if (e!=a or f!=b) and (e!=c or f!=d):
                break
        for x in range(1,8):
            for y in range(1,8):
                if x%2!=0 and y%2!=0:
                    print("+",end=" ")
                elif x%2!=0 and y%2==0:
                    print("~",end=" ")
                elif x%2==0 and y%2!=0:
                    print("|",end=" ")
                elif x==c*2 and y==d*2:
                    print("O",end=" ")
                elif x==a*2 and y==b*2:
                    print("X",end=" ")
                elif x==e*2 and y==f*2:
                    print("X",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    elif z==5:
        while 1==1:
            g=int(input("Player 0; Enter row : "))
            h=int(input("Player 0; Enter column : "))
            if (g!=a or h!=b) and (g!=c or h!=d) and (g!=e or h!=f):
                break
        for x in range(1,8):
            for y in range(1,8):
                if x%2!=0 and y%2!=0:
                    print("+",end=" ")
                elif x%2!=0 and y%2==0:
                    print("~",end=" ")
                elif x%2==0 and y%2!=0:
                    print("|",end=" ")
                elif x==c*2 and y==d*2:
                    print("O",end=" ")
                elif x==a*2 and y==b*2:
                    print("X",end=" ")
                elif x==e*2 and y==f*2:
                    print("X",end=" ")
                elif x==g*2 and y==h*2:
                    print("O",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    elif z==6:
        while 1==1:
            i=int(input("Player X; Enter row : "))
            j=int(input("Player X; Enter column : "))
            if (i!=a or j!=b) and (i!=c or j!=d) and (i!=e or j!=f) and (i!=g or j!=h):
                break
        for x in range(1,8):
            for y in range(1,8):
                if x%2!=0 and y%2!=0:
                    print("+",end=" ")
                elif x%2!=0 and y%2==0:
                    print("~",end=" ")
                elif x%2==0 and y%2!=0:
                    print("|",end=" ")
                elif x==c*2 and y==d*2:
                    print("O",end=" ")
                elif x==a*2 and y==b*2:
                    print("X",end=" ")
                elif x==e*2 and y==f*2:
                    print("X",end=" ")
                elif x==i*2 and y==j*2:
                    print("X",end=" ")
                elif x==g*2 and y==h*2:
                    print("O",end=" ")
                else:
                    print(" ",end=" ")
            print("")
        if (a==e and e==i) or (b==f and f==j) or (a==b and e==f and i==j):
            print("Player X wins")
            break
        elif (a==b or e==f or i==j) and ((a==1 and b==3) or (e==1 and f==3) or (i==1 and j==3)) and ((a==3 and b==1) or (e==3 and f==1) or (i==3 and j==1)):
            print("Player X wins")
            break
    elif z==7:
        while 1==1:
            k=int(input("Player 0; Enter row : "))
            l=int(input("Player 0; Enter column : "))
            if (k!=a or l!=b) and (k!=c or l!=d) and (k!=e or l!=f) and (k!=g or l!=h) and (k!=i or l!=j):
                break
        for x in range(1,8):
            for y in range(1,8):
                if x%2!=0 and y%2!=0:
                    print("+",end=" ")
                elif x%2!=0 and y%2==0:
                    print("~",end=" ")
                elif x%2==0 and y%2!=0:
                    print("|",end=" ")
                elif x==c*2 and y==d*2:
                    print("O",end=" ")
                elif x==a*2 and y==b*2:
                    print("X",end=" ")
                elif x==e*2 and y==f*2:
                    print("X",end=" ")
                elif x==i*2 and y==j*2:
                    print("X",end=" ")
                elif x==g*2 and y==h*2:
                    print("O",end=" ")
                elif x==k*2 and y==l*2:
                    print("O",end=" ")
                else:
                    print(" ",end=" ")
            print("")
        if (c==g and g==k) or (d==h and h==l) or (c==d and g==h and k==l):
            print("Player 0 wins")
            break
        elif (c==d or g==h or k==l) and ((c==1 and d==3) or (g==1 and h==3) or (k==1 and l==3)) and ((c==3 and d==1) or (g==3 and h==1) or (k==3 and l==1)):
            print("Player 0 wins")
            break
    elif z==8:
        while 1==1:
            m=int(input("Player X; Enter row : "))
            n=int(input("Player X; Enter column : "))
            if (m!=a or n!=b) and (m!=c or n!=d) and (m!=e or n!=f) and (m!=g or n!=h) and (m!=i or n!=j) and (m!=k or n!=l):
                break
        for x in range(1,8):
            for y in range(1,8):
                if x%2!=0 and y%2!=0:
                    print("+",end=" ")
                elif x%2!=0 and y%2==0:
                    print("~",end=" ")
                elif x%2==0 and y%2!=0:
                    print("|",end=" ")
                elif x==c*2 and y==d*2:
                    print("O",end=" ")
                elif x==a*2 and y==b*2:
                    print("X",end=" ")
                elif x==e*2 and y==f*2:
                    print("X",end=" ")
                elif x==i*2 and y==j*2:
                    print("X",end=" ")
                elif x==g*2 and y==h*2:
                    print("O",end=" ")
                elif x==k*2 and y==l*2:
                    print("O",end=" ")
                elif x==m*2 and y==n*2:
                    print("X",end=" ")
                else:
                    print(" ",end=" ")
            print("")
        if (a==m and m==i) or (b==n and n==j) or (a==b and m==n and i==j) or (e==m and m==i) or (f==n and n==j) or (e==f and m==n and i==j):
            print("Player X wins")
            break
        elif (a==b or e==f or i==j or m==n) and ((a==1 and b==3) or (e==1 and f==3) or (i==1 and j==3) or (m==1 and n==3)) and ((a==3 and b==1) or (e==3 and f==1) or (i==3 and j==1) or (m==3 and n==1)):
            print("Player X wins")
            break
    elif z==9:
        while 1==1:
            o=int(input("Player 0; Enter row : "))
            p=int(input("Player 0; Enter column : "))
            if (o!=a or p!=b) and (o!=c or p!=d) and (o!=e or p!=f) and (o!=g or p!=h) and (o!=i or p!=j) and (o!=k or p!=l) and (o!=m or p!=n):
                break
        for x in range(1,8):
            for y in range(1,8):
                if x%2!=0 and y%2!=0:
                    print("+",end=" ")
                elif x%2!=0 and y%2==0:
                    print("~",end=" ")
                elif x%2==0 and y%2!=0:
                    print("|",end=" ")
                elif x==c*2 and y==d*2:
                    print("O",end=" ")
                elif x==a*2 and y==b*2:
                    print("X",end=" ")
                elif x==e*2 and y==f*2:
                    print("X",end=" ")
                elif x==i*2 and y==j*2:
                    print("X",end=" ")
                elif x==g*2 and y==h*2:
                    print("O",end=" ")
                elif x==k*2 and y==l*2:
                    print("O",end=" ")
                elif x==m*2 and y==n*2:
                    print("X",end=" ")
                elif x==o*2 and y==p*2:
                    print("O",end=" ")
                else:
                    print(" ",end=" ")
            print("")
        if (c==o and o==k) or (d==p and p==l) or (c==d and o==p and k==l) or (g==o and o==k) or (h==p and p==l) or (g==h and o==p and k==l):
            print("Player 0 wins")
            break
        elif (c==d or g==h or k==l or o==p) and ((c==1 and d==3) or (g==1 and h==3) or (k==1 and l==3) or (o==1 and p==3)) and ((c==3 and d==1) or (g==3 and h==1) or (k==3 and l==1) or (o==3 and p==1)):
            print("Player 0 wins")
            break
    elif z==10:
        while 1==1:
            q=int(input("Player X; Enter row : "))
            r=int(input("Player X; Enter column : "))
            if (q!=a or r!=b) and (q!=c or r!=d) and (q!=e or r!=f) and (q!=g or r!=h) and (q!=i or r!=j) and (q!=k or r!=l) and (q!=m or r!=n) and (q!=o or r!=p):
                break
        for x in range(1,8):
            for y in range(1,8):
                if x%2!=0 and y%2!=0:
                    print("+",end=" ")
                elif x%2!=0 and y%2==0:
                    print("~",end=" ")
                elif x%2==0 and y%2!=0:
                    print("|",end=" ")
                elif x==c*2 and y==d*2:
                    print("O",end=" ")
                elif x==a*2 and y==b*2:
                    print("X",end=" ")
                elif x==e*2 and y==f*2:
                    print("X",end=" ")
                elif x==i*2 and y==j*2:
                    print("X",end=" ")
                elif x==g*2 and y==h*2:
                    print("O",end=" ")
                elif x==k*2 and y==l*2:
                    print("O",end=" ")
                elif x==m*2 and y==n*2:
                    print("X",end=" ")
                elif x==o*2 and y==p*2:
                    print("O",end=" ")
                elif x==q*2 and y==r*2:
                    print("x",end=" ")
                else:
                    print(" ",end=" ")
            print("")
        if (e==f and i==j and q==r) or (e==f and m==n and q==r) or (i==j and m==n and q==r):
            print("Player X wins")
            break
        elif ((e==m and m==q) or (e==i and i==q) or (i==m and m==q)) or ((f==j and j==r) or (f==n and n==r) or (j==n and n==r)):
            print("Player X wins")
            break
        elif (e==f or i==j or q==r) and (((e==3 or e==1) and (f+e==4)) or ((i==3 or i==1) and (i+j==4)) or ((q==3 or q==1) and (q+r==4))):
            print("Player X wins")
            break
        elif (e==f or m==n or q==r) and (((e==3 or e==1) and (f+e==4)) or ((m==3 or n==1) and (m+n==4)) or ((q==3 or q==1) and (q+r==4))):
            print("Player X wins")
            break
        elif (i==j or m==n or q==r) and (((i==3 or i==1) and (i+j==4)) or ((m==3 or n==1) and (m+n==4)) or ((q==3 or q==1) and (q+r==4))):
            print("Player X wins")
            break
        elif (e==f or a==b or q==r) and (((e==3 or e==1) and (f+e==4)) or ((a==3 or a==1) and (a+b==4)) or ((q==3 or q==1) and (q+r==4))):
            print("Player X wins")
            break
        elif (a==b or i==j or q==r) and (((a==3 or a==1) and (a+b==4)) or ((i==3 or i==1) and (i+j==4)) or ((q==3 or q==1) and (q+r==4))):
            print("Player X wins")
            break        
        else:
	        print("Game ends in DRAW")
print("GAME OVER!")