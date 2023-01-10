import tkinter as tk
import pygame

run=False
s="active"
p="disabled"
r="disabled"
hour=0
minute=0
second=0

hs=f'{hour}' if hour>9 else f'0{hour}'
ms=f'{minute}' if minute>9 else f'0{minute}'
ss=f'{second}' if second>9 else f'0{second}'

pygame.mixer.init()

def update():
    global hour,minute,second,hs,ms,ss
    second+=1
    if second==60:
        minute+=1
        second=0
    if minute==60:
        hour+=1
        minute=0
    hs=f'{hour}' if hour>9 else f'0{hour}'
    ms=f'{minute}' if minute>9 else f'0{minute}'
    ss=f'{second}' if second>9 else f'0{second}'
    lab.config(text=hs+":"+ms+":"+ss,font=("Arial",50))
    global upd_time
    pygame.mixer.music.load("clock-ticking-2.mp3")
    pygame.mixer.music.play(loops= 2)
    upd_time=lab.after(1000,update)


def start():
    global run,s,p,r
    if not run:
        run=True
        s="disabled"
        p="active"
        r="disabled"
        stb.config(state=s)
        pab.config(state=p)
        reb.config(state=r)
        update()

def pause():
    global run,s,p,r
    if run:
        run=False
        s="active"
        p="disabled"
        r="active"
        stb.config(state=s)
        pab.config(state=p)
        reb.config(state=r)
        pygame.mixer.music.stop()
        lab.after_cancel(upd_time)

def reset():
    global run,hour,minute,second,s,p,r
    run=False
    s="active"
    p="disabled"
    r="disabled"
    stb.config(state=s)
    pab.config(state=p)
    reb.config(state=r)
    hour=0
    minute=0
    second=0
    lab.after_cancel(upd_time)
    lab.config(text="00:00:00",font=("Arial",50))

main=tk.Tk()
main.geometry("450x120")
main.title("STOP WATCH!!")
lab=tk.Label(text=hs+":"+ms+":"+ss,font=("Arial",50))
lab.pack()
stb=tk.Button(text="START",height=2,width=20,command=start,state=s,font=('Arial',9))
stb.pack(side="left")
pab=tk.Button(text="PAUSE",height=2,width=20,command=pause,state=p,font=('Arial',9))
pab.pack(side="left")
reb=tk.Button(text="RESET",height=2,width=20,command=reset,state=r,font=('Arial',9))
reb.pack(side="left")
main.mainloop()