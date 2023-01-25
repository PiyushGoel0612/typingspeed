from tkinter import *
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
label = Label(root, text = lines[0])
label.pack()
#label1=Label(root, text = lines[0][0])
#label1.pack()
entry = Entry(root, width = 50)
entry.pack()
i = 0
k = 0
def func(event):
    global i,k
    key = event.char
    if key in letters:
        if key != lines[k][i]:
            print('wrong')
        i += 1
    else:
        i -= 1
    #abel1.config(text = lines[0][i])

    if i == len(lines[k]) and i != 0:
       k += 1
       i = 0
       label.config(text= lines[k])
       entry.delete(0,END)


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',']

entry.bind('<Key>', func)


root.mainloop()




