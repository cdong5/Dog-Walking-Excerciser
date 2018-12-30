# Created by Calvin Dong - 12/30/2018
# Learning tkinter and random Library

from random import *
from tkinter import *

def exercise():
    # Reads a txt file named exercises
    # Places each line of text into a list
    # Uses the list to generate exercises
    exerciselist = []
    file = open('exercises.txt', 'r')
    for line in file:
        ex = line.strip()
        exerciselist.append(ex)
    len_exlist = int(len(exerciselist))
    ran_ex = exerciselist[randint(0,len_exlist-1)]
    return ran_ex

def num_sec_ex():
    # Creates a random number of reps to do for exercise
    ex_time = randint(10, 20)
    return ex_time

def gen_ex():
    # Creates a Label of the exercise and number of reps
    # Places into the application
    textframe = Frame(root)
    textframe.pack()
    e1 = Label(textframe, text=(f'{exercise()} for {num_sec_ex()} reps'))
    e1.pack()

def num_sec_walk():
    # Creates a random variable to tell how long to walk
    walk_time = randint(120,240)
    return walk_time

def gen_walking():
    # Generates a label to tell how long to walk for
    # Places into the application
    textframe = Frame(root)
    textframe.pack()
    e2 = Label(textframe, text=(f'Walk for {round(num_sec_walk()//60, 2)} minutes'))
    e2.pack()
    return e2

def create_list():
    # Creates a random list of exercises and walking time
    # Gets the time you have, and creates a list of exercises to fit in the time
    time = entry_box.get()
    current_time = 0
    total_time = int(time)*60
    while current_time < total_time:
        gen_walking()
        gen_ex()
        current_time += num_sec_ex()
        current_time += num_sec_walk()

# Formating and organization of the GUI
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

gen_button = Button(gen_frame, text='Generate', command= create_list)
gen_button.pack(pady=2)

root.mainloop()
