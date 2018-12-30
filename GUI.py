from random import *
from tkinter import *

def exercise():
    exerciselist = []
    file = open('exercises.txt', 'r')
    for line in file:
        ex = line.strip()
        exerciselist.append(ex)
    ran_ex = exerciselist[randint(0,len(exerciselist))]
    return ran_ex

def gen():
    textframe = Frame(root)
    textframe.pack()
    time = randint(5,15)
    e1 = Label(textframe, text=(f'{exercise()} for {time} reps'))
    e1.pack()

root = Tk()
root.title('Dog Walk Exerciser')

labelframe = Frame(root)
labelframe.pack(side=TOP)
top_label = Label(labelframe, text='Dog Walk Exerciser').pack(side=TOP)

Entry_frame = Frame(root)
Entry_frame.pack(side=TOP)

entry_label = Label(Entry_frame, text='How Long?')
entry_label.pack(side="left", padx=2)

entry_box = Entry(Entry_frame)
entry_box.pack(side="left", padx=2, pady=2)

gen_frame = Frame(root)
gen_frame.pack(side=TOP)

gen_button = Button(gen_frame, text='Generate', command=gen)
gen_button.pack(pady=2)

root.mainloop()
