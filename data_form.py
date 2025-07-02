import tkinter as tk
window=tk.Tk()
window.title("viva practice")
window.geometry("200x150")
def button_1():
    print("submit data succesfully")

name=tk.Label(window,text="name:",font=20)
name.grid(row=1,column=1)

entry=tk.Entry(window,width=30)
entry.grid(row=1,column=2)

email=tk.Label(window,text="email:",font=20)
email.grid(row=2,column=1)

email_entry=tk.Entry(window,width=30)
email_entry.grid(row=2,column=2)

submit=tk.Button(window,text="submit",command="button_1")
submit.grid(row=5,column=2)


window.mainloop()