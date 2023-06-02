#GUI code file

import tkinter as tk
import time

window = tk.Tk()
window.title('Timer lasera')


def shortSleep():
    window.quit()
    
    

label1 = tk.Label(
    window,
    text = 'Czy włączono logger lasera?',
    width = 22,
    height = 2,
    font='Times 18 bold',
    padx=10,
    pady=10,
    justify='center'
    )
label1.pack()

button1 = tk.Button(
    window,
    text='TAK +1h',
    bg='light green',
    justify='center',
    font='Times 18 bold'
)
button1.pack(side='left', expand=True,fill=tk.BOTH)

button2 = tk.Button(
    window,
    text='NIE +2 min',
    bg='red',
    font='Times 18 bold',
    command= shortSleep
)

button2.pack(side='right', expand= True,fill=tk.BOTH)

window.mainloop()