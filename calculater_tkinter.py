from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("300x450")
window.title("Simple Calculator")
window.config(pady=10,bg="grey12")
#-------------------------------COMMAND----------------------------------#

calulation = []
def equal():
    result ="".join(calulation)
    if "+" in result:
        ans = result.split("+")
        ans1 =float(ans[0])
        ans2 = float(ans[1])
        answer = ans1 + ans2
        equal_label.delete(0,END)
        equal_label.insert(END,answer)

    elif "-" in result:
        ans = result.split("-")
        ans1 = float(ans[0])
        ans2 = float(ans[1])
        answer = ans1 - ans2
        equal_label.delete(0,END)
        equal_label.insert(END,answer)

    elif "*" in result:
        ans = result.split("*")
        ans1 = float(ans[0])
        ans2 = float(ans[1])
        answer = ans1 * ans2
        equal_label.delete(0,END)
        equal_label.insert(END,answer)
    
    elif "/" in result:
        ans = result.split("/")
        ans1 = float(ans[0])
        ans2 = float(ans[1])
        answer = ans1 / ans2
        equal_label.delete(0,END)
        equal_label.insert(END,answer)

    elif "^" in result:
        ans = result.split("^")
        ans1 = float(ans[0])
        ans2 = float(ans[1])
        answer = ans1** ans2
        equal_label.delete(0,END)
        equal_label.insert(END,answer)

def clear():
    calulation.clear()
    equal_label.delete(0,END)

def plus():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"+")
    calulation.append("+")

def minus():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"-")
    calulation.append("-")

def multi():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"x")
    calulation.append("*")

def divide():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"/")
    calulation.append("/")

def zero():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"0")
    calulation.append("0")

def one():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"1")
    calulation.append("1")

def two():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"2")
    calulation.append("2")

def three():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"3")
    calulation.append("3")

def four():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"4")
    calulation.append("4")

def five():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"5")
    calulation.append("5")

def six():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"6")
    calulation.append("6")
def seven():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"7")
    calulation.append("7")

def eight():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"8")
    calulation.append("8")

def nine():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"9")
    calulation.append("9")

def point():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+".")
    calulation.append(".")

def square():
    current = equal_label.get()
    equal_label.delete(0,END)
    equal_label.insert(0, str(current)+"^")
    calulation.append("^")

#---------------------------------GUI------------------------------------#

equal_label = ttk.Entry(window,font=('arial', 30), width=10)
equal_label.config()
equal_label.place(x=34,y=20)

button_7 = Button(text="7",bg="black",width=5,height=3,highlightthickness=1,fg="White",command=seven)
button_7.place(x=35,y=85)

button_8 = Button(text="8",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=eight)
button_8.place(x=95,y=85)

button_9 = Button(text="9",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=nine)
button_9.place(x=155,y=85)

button_4 = Button(text="4",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=four)
button_4.place(x=35,y=150)

button_5 = Button(text="5",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=five)
button_5.place(x=95,y=150)

button_6 = Button(text="6",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=six)
button_6.place(x=155,y=150)

button_plus = Button(text="+",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=plus)
button_plus.place(x=215,y=150)

button_1 = Button(text="1",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=one)
button_1.place(x=35,y=215)

button_2 = Button(text="2",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=two)
button_2.place(x=95,y=215)

button_3 = Button(text="3",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=three)
button_3.place(x=155,y=215)

button_0 = Button(text="0",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=zero)
button_0.place(x=95,y=280)

button_clear = Button(text="Clear",bg="black",width=5,height=3,highlightthickness=1,fg="White",command=clear)
button_clear.place(x=215,y=85)

button_minus = Button(text="-",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=minus)
button_minus.place(x=215,y=215)

button_divide = Button(text="/",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=divide)
button_divide.place(x=35,y=280)

button_multi = Button(text="x",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=multi)
button_multi.place(x=215,y=280)

button_equal = Button(text="equal",bg="slateblue1",width=22,height=3,highlightthickness=1,fg="black",command=equal)
button_equal.place(x=95,y=340)

button_point = Button(text=".",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=point)
button_point.place(x=155,y=280)

button_square = Button(text="^",bg="Black",width=5,height=3,highlightthickness=1,fg="White",command=square)
button_square.place(x=35,y=340)

window.mainloop()