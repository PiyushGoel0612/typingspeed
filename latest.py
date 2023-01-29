from tkinter import *
import words

wrd_st=set(words.a1)
wrd=list(wrd_st)
root=Tk()
var=StringVar()
l=0
m=0
over=0
mistake=0
ev_c=0
sec=60
min=0
ch=0
nope=['Control_L','Control_R','Alt_L','Alt_R','Shift_L','Shift_R','Return',
    'Caps_Lock','Tab','Left','Right','Up','Down','Prior','Next','Delete']

def restart():
    global wrd_st,wrd,l,m,over,mistake,ev_c,sec,min,ch
    wrd_st=set(words.a1)
    wrd=list(wrd_st)
    l=0
    m=0
    over=0
    mistake=0
    ev_c=0
    sec=60
    min=0
    ch=0
    bre.destroy()
    t1.config(state='normal')
    t1.delete('1.0','end')
    t1.insert('1.0',wrd[0:13])
    t1.tag_add('tn','1.0','end')
    t1.config(state='disabled')
    lb2.config(text=wrd[13:26])
    lb3.config(text=wrd[m][l],bg='#FFF200')
    lbt.config(text='01:00',bg='cadetblue3')
    en1=Entry(f2,textvariable=var,width=60,font=('Arial',15))
    en1.grid(padx=5,pady=10,row=0,column=0)
    en1.bind('<Key>',tak)
    
def tak(event):
    global l,m,over,mistake,ev_c,sec,min,ch,nope
    def inner():
        global sec,min
        sec-=1
        ss=f'{sec}' if sec>9 else f'0{sec}'
        ms=f'{min}' if min>9 else f'{min}'
        lbt.config(text=ms+':'+ss)
        if sec==0:
            wc=(m+l/m)*60/59
            en1.unbind(event)
            en1.delete(0,END)
            lbt.config(text="",bg='#FFA500')
            t1.config(state='normal')
            t1.delete('1.0','end')
            t1.insert('1.0',"Your time's up")
            t1.tag_add('soo','1.0','end')
            t1.tag_config('soo',justify='center')
            t1.config(state='disabled')
            lb2.config(text="Your typing Speed is "+str(wc)[0:4]+" words per minute")
            lb3.config(text='',bg='#FFA500')
            en1.destroy()
            bre.grid(padx=5,pady=10,row=0,column=1)
        if sec!=0:
            global ko
            ko=lbt.after(1000,inner)
    if ev_c==0:
        ev_c=1
        inner()
    typed=event.keysym
    
    if typed not in nope:
        if mistake==0 and over==0:
            if typed=='space':
                mistake=1
                t1.config(state='normal')
                t1.insert('1.'+str(ch),' ')
                t1.tag_add('er','1.'+str(ch),'1.'+str(ch+1))
                t1.tag_config('er',background='red')
                t1.config(state='disabled')
                print('mistake')
            elif typed=='BackSpace':
                if l!=0:
                    l-=1
                else:
                    over=1
                    m-=1
                    l=len(wrd[m-1])-1
                ch-=1
            elif typed==wrd[m][l]:
                if l!=len(wrd[m])-1:
                    l+=1
                else:
                    over=1
                ch+=1
            elif typed!=wrd[m][l]:
                mistake+=1
                t1.config(state='normal')
                t1.insert('1.'+str(ch),event.char)
                t1.tag_add('er','1.'+str(ch),'1.'+str(ch+1))
                t1.tag_config('er',background='red')
                t1.config(state='disabled')
                print('mistake')
        
        elif mistake!=0 and over==0:
            if typed=='BackSpace':
                mistake-=1
                t1.config(state='normal')
                t1.tag_remove('er','1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
                if mistake!=0:
                    t1.tag_add('er','1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
                    t1.tag_config('er',background='red')
                t1.delete('1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
                t1.config(state='disabled')
            else:
                mistake+=1
                t1.config(state='normal')
                t1.insert('1.'+str(ch+mistake-1),event.char)
                t1.tag_add('er','1.'+str(ch+mistake-1),'1.'+str(ch+mistake))
                t1.tag_config('er',background='red')
                t1.config(state='disabled')
                print('mistake')
        
        elif mistake==0 and over==1:
            if typed=='space':
                over=0
                m+=1
                l=0
                ch+=1
            elif typed=='BackSpace':
                over=0
                ch-=1
            else:
                mistake+=1
                t1.config(state='normal')
                t1.insert('1.'+str(ch+mistake-1),event.char)
                t1.tag_add('er','1.'+str(ch+mistake-1),'1.'+str(ch+mistake))
                t1.tag_config('er',background='red')
                t1.config(state='disabled')
                print('mistake')
        
        elif mistake!=0 and over==1:
            if typed=='BackSpace':
                mistake-=1
                t1.config(state='normal')
                t1.tag_remove('er','1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
                if mistake!=0:
                    t1.tag_add('er','1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
                    t1.tag_config('er',background='red')
                t1.delete('1.'+str(ch+mistake),'1.'+str(ch+mistake+1))
                t1.config(state='disabled')
            else:
                mistake+=1
                t1.config(state='normal')
                t1.insert('1.'+str(ch+mistake-1),event.char)
                t1.tag_add('er','1.'+str(ch+mistake-1),'1.'+str(ch+mistake))
                t1.tag_config('er',background='red')
                t1.config(state='disabled')
                print('mistake')
        
        if over!=1:
            lb3.config(text=wrd[m][l])
        else:
            lb3.config(text='_')

        if m%13==0 and l==0 and m<74 and m!=0:
            t1.config(state="normal")
            t1.tag_delete('tn','1.0','end')
            t1.tag_config('tn',justify='center')
            t1.delete('1.0','end')
            t1.insert('1.0',wrd[m:m+13])
            t1.tag_add('tn','1.0','end')
            lb2.config(text=wrd[m+13:m+26])
            en1.delete(0,END)
            ch=0

root.geometry('800x300')
root.title('Typing_Practice')
root.config(background='#FFA500')

f1=Frame(root,background='#FFA500')
f1.grid(pady=10,padx=10)
f2=Frame(root,background='#FFA500')
f2.grid(pady=10,padx=10)
f3=Frame(root,background='#FFA500')
f3.grid(pady=10,padx=10)

t1=Text(f1,font=('Arial',15),height=1,width=60,relief='flat',bg='#FFF200')
t1.tag_config('tn',justify='center')
t1.insert('1.0',wrd[0:13])
t1.tag_add('tn','1.0','end')
t1.config(state='disabled')
t1.grid(pady=10,padx=10)

lb2=Label(f1,text=wrd[13:26],font=('Arial',15),bg='#FFF200')
lb2.grid(padx=10,pady=10)
en1=Entry(f2,textvariable=var,width=60,font=('Arial',15))
en1.grid(padx=5,pady=10,row=0,column=0)
lb3=Label(f3,text=wrd[m][l],font=('Arial',15),bg='#FFF200')
lbt=Label(f2,text='01:00',width=8,font=('Arial',15),background='cadetblue3')
lbt.grid(padx=5,pady=10,row=0,column=1)
lb3.pack(side='top')
bre=Button(f2,text='Restart',command=restart,bg='yellow',font=('Arial',15))

en1.bind('<Key>',tak)

root.mainloop()