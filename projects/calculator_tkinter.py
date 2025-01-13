import tkinter
from tkinter import *
from tkinter import messagebox
var = ""
A = 0
operator = ""
def button_0_is_clicked():
  global var
  var = var+"0"
  the_data.set(var)
def button_1_is_clicked():
  global var
  var = var+"1"
  the_data.set(var)
def button_2_is_clicked():
  global var
  var = var+"2"
  the_data.set(var)
def button_3_is_clicked():
  global var
  var = var+"3"
  the_data.set(var)
def button_4_is_clicked():
  global var
  var = var+"4"
  the_data.set(var)
def button_5_is_clicked():
  global var
  var = var+"5"
  the_data.set(var)
def button_6_is_clicked():
  global var
  var = var+"6"
  the_data.set(var)
def button_7_is_clicked():
  global var
  var = var+"7"
  the_data.set(var)
def button_8_is_clicked():
  global var
  var = var+"8"
  the_data.set(var)
def button_9_is_clicked():
  global var
  var = var+"9"
  the_data.set(var)
def button_add_is_clicked():
  global A, var, operator
  A = float(var)
  operator = "+"
  var = var+"+"
  the_data.set(var)
def button_sub_is_clicked():
  global A, var, operator
  A = float(var)
  operator = "-"
  var = var+"-"
  the_data.set(var)
def button_mul_is_clicked():
  global A, var, operator
  A = float(var)
  operator = "*"
  var = var+"*"
  the_data.set(var)
def button_div_is_clicked():
  global A, var, operator
  A = float(var)
  operator = "/"
  var = var+"/"
  the_data.set(var)
def button_equal_is_clicked():
  global A, var, operator
  A = float(var)
  operator = "="
  var = var+"="
  the_data.set(var)
def button_c_is_clicked():
  global A, var, operator
  A = 0
  operator = ""
  var = ""
  the_data.set(var)
def button_pwr_is_clicked():
  global A, var, operator
  A = float(var)
  operator = "^"
  var = var+"^"
  the_data.set(var)
def res():
  global A, var, operator
  var2 = var
  if operator == "+":
    a = float((var2.split("+")[1]))
    x = A + a
    the_data.set(x)
    var = str(x)
  elif operator == "-":
    a = float((var2.split("-")[1]))
    x = A - a
    the_data.set(x)
    var = str(x)
  elif operator == "*":
    a = float((var2.split("*")[1]))
    x = A * a
    the_data.set(x)
    var = str(x)
  elif operator == "/":
    a = float((var2.split("/")[1]))
    if a == 0:
      messagebox.showerror("Division by 0 not allowed.")
      A == ""
      var = ""
      the_data.set(var)
    else:
      x = float(A/a)
      the_data.set(x)
      var = str(x)
  elif operator == "^":
    a = float((var2.split("^")[1]))
    x = float(A**a)
    the_data.set(x)
    var = str(x)

win = tkinter.Tk()
win.geometry("380x560+460+460")
win.resizable(0,0)
win.title("Calculator")
the_data = StringVar()
winlabel = Label(win, text = "label", anchor=SE, font=("Arial",20), textvariable=the_data, bg="#ff0000", fg="#000000")
winlabel.pack(expand=True, fill="both") 
frame1=Frame(win, bg="#000000")
frame1.pack(expand=True, fill="both")
frame2=Frame(win, bg="#000000")
frame2.pack(expand=True, fill="both")
frame3=Frame(win, bg="#000000")
frame3.pack(expand=True, fill="both")
frame4=Frame(win, bg="#000000")
frame4.pack(expand=True, fill="both")
button1 = Button(frame1, text="1", font=("Arial",20),relief=GROOVE, border=0, command=button_1_is_clicked)
button1.pack(side=LEFT, expand=True, fill="both")
button2 = Button(frame1, text="2", font=("Arial",20),relief=GROOVE, border=0, command=button_2_is_clicked)
button2.pack(side=LEFT, expand=True, fill="both")
button3 = Button(frame1, text="3", font=("Arial",20),relief=GROOVE, border=0, command=button_3_is_clicked)
button3.pack(side=LEFT, expand=True, fill="both")
buttonc = Button(frame1, text="C", font=("Arial",20),relief=GROOVE, border=0, command=button_c_is_clicked)
buttonc.pack(side=LEFT, expand=True, fill="both")
button4 = Button(frame2, text="4", font=("Arial",20),relief=GROOVE, border=0, command=button_4_is_clicked)
button4.pack(side=LEFT, expand=True, fill="both")
button5 = Button(frame2, text="5", font=("Arial",20),relief=GROOVE, border=0, command=button_5_is_clicked)
button5.pack(side=LEFT, expand=True, fill="both")
button6 = Button(frame2, text="6", font=("Arial",20),relief=GROOVE, border=0, command=button_6_is_clicked)
button6.pack(side=LEFT, expand=True, fill="both")
buttonadd = Button(frame2, text="+", font=("Arial",20),relief=GROOVE, border=0, command=button_add_is_clicked)
buttonadd.pack(side=LEFT, expand=True, fill="both")
button7 = Button(frame3, text="7", font=("Arial",20),relief=GROOVE, border=0, command=button_7_is_clicked)
button7.pack(side=LEFT, expand=True, fill="both")
button8 = Button(frame3, text="8", font=("Arial",20),relief=GROOVE, border=0, command=button_8_is_clicked)
button8.pack(side=LEFT, expand=True, fill="both")
button9 = Button(frame3, text="9", font=("Arial",20),relief=GROOVE, border=0, command=button_9_is_clicked)
button9.pack(side=LEFT, expand=True, fill="both")
buttonsub = Button(frame3, text="-", font=("Arial",20),relief=GROOVE, border=0, command=button_sub_is_clicked)
buttonsub.pack(side=LEFT, expand=True, fill="both")
button0 = Button(frame4, text="0", font=("Arial",20),relief=GROOVE, border=0, command=button_0_is_clicked)
button0.pack(side=LEFT, expand=True, fill="both")
buttonmul = Button(frame4, text="*", font=("Arial",20),relief=GROOVE, border=0, command=button_mul_is_clicked)
buttonmul.pack(side=LEFT, expand=True, fill="both")
buttondiv = Button(frame4, text="/", font=("Arial",20),relief=GROOVE, border=0, command=button_div_is_clicked)
buttondiv.pack(side=LEFT, expand=True, fill="both")
buttonequal = Button(frame4, text="=", font=("Arial",20),relief=GROOVE, border=0, command=res)
buttonequal.pack(side=LEFT, expand=True, fill="both")
buttonpwr = Button(frame4, text="^", font=("Arial",20),relief=GROOVE, border=0, command=button_pwr_is_clicked)
buttonpwr.pack(side=LEFT, expand=True, fill="both")
win.mainloop()


