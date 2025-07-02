#Hello World Gui 

import tkinter as tk
window=tk.Tk()
window.title("Hello World Gui")
window.geometry("400x200")
def on_click():
    print("Run Succesfully")

    
label=tk.Label(window,text="HELLO WORLD",font=25)
label.place(x=100,y=70)


btn=tk.Button(window,text="Run Gui",command=on_click)
btn.place(x=150,y=105)
window.mainloop()