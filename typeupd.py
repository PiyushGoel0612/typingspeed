from tkinter import *
import words
import time
from multiprocessing import Process

wrd_st=set(words.a1)
wrd=list(wrd_st)
root=Tk()
var=StringVar()
l=0
m=0
over=0
mistake=0
ev_c=0
sec=0
min=0

def tak(event):
    global l,m,over,mistake,ev_c,sec,min
    def inner():
        global sec,min
        sec+=1
        if sec==60:
            minute+=1
            sec=0
        ss=f'{sec}' if sec>9 else f'0{sec}'
        ms=f'{min}' if min>9 else f'{min}'
        lbt.config(text=ms+':'+ss)
        global ko
        ko=lbt.after(1000,inner)
    if ev_c==0:
        x=time.time()
        ev_c=1
        inner()
    typed=event.keysym
    if mistake==0 and over==0:
        if typed=='space':
            mistake=1
            print('mistake')
        elif typed=='BackSpace':
            if l!=0:
                l-=1
            else:
                over=1
                m-=1
                l=len(wrd[m-1])-1
        elif typed==wrd[m][l]:
            if l!=len(wrd[m])-1:
                l+=1
            else:
                over=1
        elif typed!=wrd[m][l]:
            mistake+=1
            print('mistake')
    elif mistake!=0 and over==0:
        if typed=='BackSpace':
            mistake-=1
        else:
            mistake+=1
            print('mistake')
    elif mistake==0 and over==1:
        if typed=='space':
            over=0
            m+=1
            l=0
        elif typed=='BackSpace':
            over=0
        else:
            mistake+=1
            print('mistake')
    elif mistake!=0 and over==1:
        if typed=='BackSpace':
            mistake-=1
        else:
            mistake+=1
            print('mistake')
    
    if over!=1:
        lb3.config(text=wrd[m][l])
    else:
        lb3.config(text='_')

    if m%13==0 and l==0 and m<74:
        lb1.config(text=wrd[m:m+13])
        lb2.config(text=wrd[m+13:m+26])
        en1.delete(0,END)

root.geometry('800x500')
root.title('Typing_Practice')

f1=Frame(root)
f1.pack(side='top')
f2=Frame(root)
f2.pack(side='top')
f3=Frame(root)
f3.pack(side='top')
lb1=Label(f1,text=wrd[0:13],font=('Arial',15))
lb1.pack()
lb2=Label(f1,text=wrd[13:26],font=('Arial',15))
lb2.pack(side='top')
en1=Entry(f2,textvariable=var,width=60,font=('Arial',15))
en1.pack(side='left')
lb3=Label(f3,text=wrd[m][l],font=('Arial',15))
lbt=Label(f2,text='00:00',width=8,font=('Arial',15))
lbt.pack(side='left')
lb3.pack(side='top')

en1.bind('<Key>',tak)

root.mainloop()