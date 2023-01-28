from tkinter import *
import datetime
import wordsList
words_set = set(wordsList.words_list)
words_final_list = list(words_set)
a = ''
lines = []
for i,k in enumerate(words_final_list):
    a += k.lower() + ' '
    if i % 11 == 0 and i != 0: 
        lines.append(a)
        a = ''
    elif i == 150:
        break


root = Tk()
root.geometry('1000x400')
var = StringVar()
# label = Label(root, text = lines[0])
# label.pack()


frame = Frame(root)
frame.pack()
x  = []

for l in range(12):
    label = Label(frame, text = lines[0].split()[l])
    label.pack(side= 'left')
    x.append(label)

def red_white(k=0):
    if k == 0:
        x[0].config(bg= 'red')

    else:
        x[0].config(bg= 'black')



def change_labels(k):
    for j in range(12):
        x[i].config(text = lines[k].split()[j])


entry = Entry(root, width = 50)
entry.pack()

button1 = Button(root, text = 'red', command= red_white)
button1.pack()

button2 = Button(root, text= 'normal', command= lambda : red_white(1))
button2.pack()


# i = 0
# k = 0
# def func(event):
#     global i,k
#     key = event.char
#     if key in letters:
#         if key != :
#             print('wrong')
#         i += 1
#         print(i)
#     elif entry.get() == lines[k]:
#             k += 1
#             i = 0
#             x[0].config(text = lines[k][i])
#             entry.delete(0,END)
#     else:
#         i -= 1
      

# letters = ['[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',', "'"]

# entry.bind('<Key>', func)


root.mainloop()




