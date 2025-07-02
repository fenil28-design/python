#calculator using tkinter with gui app

import tkinter as tk

def add():
    total.set(float(entry_1.get()) +float(entry_2.get()))
def sub():
    total.set(float(entry_1.get())-float(entry_2.get()))
    
def mul():
    total.set(float(entry_1.get())*float(entry_2.get()))
def div():
    try:
        total.set(float(entry_1.get()) / float(entry_2.get()))
    except ZeroDivisionError:
        total.set("error: Division by zero")
        
window=tk.Tk()
window.title("Simple Calculator")

lbl1=tk.Label(window,text=" Enter The Number 1")
lbl1.grid(row=0,column=0)
entry_1=tk.Entry(window)
entry_1.grid(row=0,column=1)  

lbl2=tk.Label(window,text=" Enter The Number 2")
lbl2.grid(row=1,column=0)
entry_2=tk.Entry(window)
entry_2.grid(row=1,column=1)  

total=tk.Label(window,text="Total")
total.grid(row=2,column=0)
total=tk.StringVar()

entry_total=tk.Entry(window,textvariable=total)
entry_total.grid(row=2,column=1)

btn1=tk.Button(window,text="+",width=5,command=add)
btn2=tk.Button(window,text="-",width=5,command=sub) 
btn3=tk.Button(window,text="*",width=5,command=mul)
btn4=tk.Button(window,text="/",width=5,command=div)
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=4,column=0)
btn4.grid(row=4,column=1)


window.mainloop()