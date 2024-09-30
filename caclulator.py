from tkinter import *

def button_click(num):

    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equal_to():

    global equation_text

    try:
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text= total

    except ZeroDivisionError:
        equation_label.set("error")
        equation_text= ""

    except SyntaxError:
        equation_label.set("error")
        equation_text= ""


def clear():
    global equation_text

    equation_label.set("")

    equation_text= ""


window = Tk()
window.title("Calculator")
window.geometry("600x600")
window.configure(bg='grey')

equation_text= ""

equation_label = StringVar()


label = Label(window, textvariable=equation_label, font=("consolas", 20), fg= "green", bg="black", width = 27, height=3)
label.pack()

frame=Frame(window)
frame.pack()

button1= Button(frame, text=1, height= 4, width= 9, font=35 ,command=lambda: button_click(1),bg="grey")

button1.grid(row=0, column=0)

button2= Button(frame, text=2, height= 4, width= 9, font=35,command=lambda: button_click(2),bg="grey")

button2.grid(row=0, column=1)

button3= Button(frame, text=3, height= 4, width= 9, font=35,command=lambda: button_click(3),bg="grey")

button3.grid(row=0, column=2)

button4= Button(frame, text=4, height= 4, width= 9, font=35,command=lambda: button_click(4),bg="grey")

button4.grid(row=1, column=0)

button5= Button(frame, text=5, height= 4, width= 9, font=35,command=lambda: button_click(5), bg="grey")

button5.grid(row=1, column=1)

button6= Button(frame, text=6, height= 4, width= 9, font=35,command=lambda: button_click(6), bg="grey")

button6.grid(row=1, column=2)

button7= Button(frame, text=7, height= 4, width= 9, font=35,command=lambda: button_click(7), bg="grey")

button7.grid(row=2, column=0)

button8= Button(frame, text=8, height= 4, width= 9, font=35,command=lambda: button_click(8), bg="grey")

button8.grid(row=2, column=1)

button9= Button(frame, text=9, height= 4, width= 9, font=35,command=lambda: button_click(9), bg="grey")

button9.grid(row=2, column=2)

button0= Button(frame, text=0, height= 4, width= 9, font=35,command=lambda: button_click(0), bg="grey")

button0.grid(row=3, column=0)

plus= Button(frame, text="+", height= 4, width= 9, font=35,command=lambda: button_click("+"), bg="grey")

plus.grid(row=0, column=3)

minus= Button(frame, text="-", height= 4, width= 9, font=35,command=lambda: button_click("-"), bg="grey")

minus.grid(row=1, column=3)

multiply= Button(frame, text="*", height= 4, width= 9, font=35,command=lambda: button_click("*"), bg="grey")

multiply.grid(row=2, column=3)

division= Button(frame, text="/", height= 4, width= 9, font=35,command=lambda: button_click("/"), bg="grey")

division.grid(row=3, column=3)

equal= Button(frame, text="=", height= 4, width= 9, font=35, command=equal_to, bg="grey")

equal.grid(row=3, column=2)

decimal= Button(frame, text=".", height= 4, width= 9, font=35,command=lambda: button_click("."), bg="grey")

decimal.grid(row=3, column=1)

clear= Button(window, text="clear", height= 4, width= 19, font=35, command= clear, bg="grey")

clear.pack()

window.mainloop()