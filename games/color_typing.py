import tkinter
from tkinter import *
import random

color = ["Red","Green","Blue","Yellow","Black","Purple","Orange","Pink","Brown","White"]
score = 0
time_left = 30
def start_game(event):
  if time_left==30:
    countdown()
  nextcolor()
def nextcolor():
  global score
  global time_left
  if time_left>0:
    e.focus_set()
    if e.get().lower() == color[1].lower():
      score+=1
    e.delete(0,tkinter.END)
    random.shuffle(color)
    label.config(fg=str(color[1]),text=str(color[0]))
    scorelabel.config(text="SCORE: "+str(score))
def countdown():
  global time_left
  if time_left>0:
    time_left-=1
    timeLabel.config(text="TIME LEFT: "+str(time_left))
    timeLabel.after(1000,countdown)

win = Tk()
win.title("Color Game")
win.geometry("375x200")
instruction = Label(win,text="Type Color of the word, not the word itself.", font=("Arial",12))
instruction.pack()
scorelabel = Label(win, text = "Press Enter to Start", font=("Arial",12))
scorelabel.pack()
timelabel = Label(win, text = "Time Left", font=("Arial",12))
timelabel.pack()
label = Label(win, font=("Arial",12))
label.pack()
e = Entry(win)
win.bind('<Return>', start_game)
e.pack()
e.focus_set()
win.mainloop()
