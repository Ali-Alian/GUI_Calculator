from tkinter import *


exp = " "

def press(num):
    global exp
    exp=exp+str(num)
    equation.set(exp)
    
def result():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = " "
    except:
        equation.set('error')
        exp = " "


def clear ():
    global exp
    exp = " "
    equation.set(" ")

window = Tk()

window.wm_iconbitmap("calc.ico")


# Calculator View 
equation=StringVar()
output_box = Entry(window, width = 36, textvariable = equation)
output_box.grid(row=0, column=0, rowspan=1, columnspan=10)

b7=Button(window, text="7", width=5, command = lambda : press(7))
b7.grid(row=1, column=0)

b8=Button(window, text="8", width=5, command = lambda : press(8))
b8.grid(row=1, column=1)

b9=Button(window, text="9", width=5, command = lambda : press(9))
b9.grid(row=1, column=2)

sub=Button(window, text="-", width=5, command = lambda : press("-"))
sub.grid(row=1, column=3)

multi=Button(window, text="x", width=5, command = lambda : press("*"))
multi.grid(row=1, column=4)

b4=Button(window, text="4", width=5, command = lambda : press(4))
b4.grid(row=2, column=0)

b5=Button(window, text="5", width=5, command = lambda : press(5))
b5.grid(row=2, column=1)

b6=Button(window, text="6", width=5, command = lambda : press(6))
b6.grid(row=2, column=2)

add=Button(window, text="+", width=5, command = lambda : press("+"))
add.grid(row=2, column=3)

dvid=Button(window, text="/", width=5,command = lambda : press("/"))
dvid.grid(row=2, column=4)

b3=Button(window, text="3", width=5, command = lambda : press(3))
b3.grid(row=3, column=0)

b2=Button(window, text="2", width=5, command = lambda : press(2))
b2.grid(row=3, column=1)

b1=Button(window, text="1", width=5, command = lambda : press(1))
b1.grid(row=3, column=2)

clear=Button(window, text="C", width=5, command = clear)
clear.grid(row=3, column=3)

result=Button(window, text="=", width=5, command = result)
result.grid(row=3, column=4)

b0=Button(window, text="0", height=1, width=31, command = lambda : press(0))
b0.grid(row=4, column=0, rowspan=1, columnspan=10)

window.mainloop()