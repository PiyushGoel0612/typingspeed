from tkinter import *
import time
import wordsList

te='everytime i see someone spell a word wrong i look down at the keyboard and see how close the wrong letter is to the correct one'

words = set(wordsList.words_list)

for i in words:
    print(i, end = " ")

screen=Tk()

l=0
lft=''
rig=te[0:20]
disp=te[0]
m=0
kl="""everytime i see someone spell a word 
wrong i look down at the keyboard and see
how close the wrong letter is to the correct one"""

def tak(event):
    global lft,rig,l,disp,m
    key=event.char
    if l==1:
        m=time.perf_counter()
    if key==rig[0]:
        if (l+1)<len(te):
            if l>20:
                lft=te[(l-20):(l+1)]
            else:
                if disp!="_":
                    lft=lft+disp
                else:
                    lft=lft+" "
            l+=1
            rig=te[l:l+20]
            if rig[0]!=' ':
                disp=rig[0]
            else:
                disp="_"
            l1.config(text=lft)
            l2.config(text=rig)
            l4.config(text=disp)
        else:
            lft=te[(l-20):(l-1)]
            rig=''
            y=time.perf_counter()
            disp=str((1560/(y-m)).__round__(2))+' words per minute'
            l1.config(text=lft)
            l2.config(text=rig)
            l4.config(text=disp)

ln=Label(screen,height=4,width=65,text=kl,font=('Arial',15),anchor=N)
l1=Label(screen,background='red',height=2,width=32,text=lft,font=('Arial',15),anchor=E)
l2=Label(screen,background='green',height=2,width=32,text=rig,font=('Arial',15),anchor=W)
l3=Label(screen,height=2,width=0,font=('Arial',15))
l4=Label(screen,background='blue',height=2,width=63,text=disp,font=('Arial',15))

l4.pack(side='top')
ln.pack(side='top')
l1.pack(side='left')
l3.pack(side='left')
l2.pack(side='left')

screen.bind('<Key>',tak)
screen.mainloop()
