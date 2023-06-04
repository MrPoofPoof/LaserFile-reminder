#GUI and commands code

import tkinter as tk
import time
import math

#first window creator 
def createYesNoWindow():
    #first window constructor
    yesNoWindow = tk.Tk()
    yesNoWindow.title('Timer lasera')

    #Set window to appear in the middle
    windowWidth = 330
    windowHeight = 122
    screenWidth = yesNoWindow.winfo_screenwidth()
    screenHeight = yesNoWindow.winfo_screenheight()

    x_pos = math.floor((screenWidth - windowWidth) / 2)
    y_pos = math.floor(((screenHeight - windowHeight) / 2) * 0.80)

    yesNoWindow.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")

    #NO button command
    def no():
        yesNoWindow.withdraw()
        time.sleep(2)  #2 minuty = 120
        yesNoWindow.deiconify()

    #YES button command
    def yes():
        yesNoWindow.withdraw()
        time.sleep(2) #1h = 3600
        createYesWindow()
        yesNoWindow.destroy()

    #Labels and Buttons for first window
    isLoggerOn = tk.Label(
        yesNoWindow,
        text = 'Czy włączono logger lasera?',
        width = 22,
        height = 2,
        font='Times 18 bold',
        padx=10,
        pady=10,
        justify='center'
        )
    isLoggerOn.pack()

    yesButton = tk.Button(
        yesNoWindow,
        text='TAK +1h',
        bg='light green',
        justify='center',
        font='Times 18 bold',
        command= yes
    )
    yesButton.pack(side='left', expand=True,fill=tk.BOTH)

    noButton = tk.Button(
        yesNoWindow,
        text='NIE +2 min',
        bg='red',
        font='Times 18 bold',
        command = no
    )
    noButton.pack(side='right', expand= True,fill=tk.BOTH)
    yesNoWindow.mainloop()


#second window creator 
def createYesWindow():
    yesWindow = tk.Tk()
    yesWindow.title('Timer lasera')

    #Set window to appear in the middle
    windowWidtg = 330
    windowHeight = 122
    screenWidth = yesWindow.winfo_screenwidth()
    screenHeight = yesWindow.winfo_screenheight()

    x_pos = math.floor((screenWidth - windowWidtg) / 2)
    y_pos = math.floor(((screenHeight - windowHeight) / 2) * 0.80)

    yesWindow.geometry(f"{windowWidtg}x{windowHeight}+{x_pos}+{y_pos}")

#OK button command
    def ok():
        yesWindow.withdraw()
        time.sleep(2) #1h = 3600
        yesWindow.deiconify()

#Label and Button for second window
    changeLog = tk.Label(
        yesWindow,
        text = 'ZMIEŃ LOG LASERA \n(nie nad linią!)',
        width = 22,
        height = 2,
        font='Times 18 bold',
        padx=10,
        pady=10,
        justify='center'
        )
    changeLog.pack()

    yesButton2 = tk.Button(
    yesWindow,
    text='OK',
    bg='light green',
    justify='center',
    font='Times 18 bold',
    command= ok
    )
    yesButton2.pack(expand=True,fill=tk.BOTH)