#GUI and commands code

import tkinter as tk
import time
import math

#first window creator 
def createInitialWindow():
    #first window constructor
    initialWindow = tk.Tk()
    initialWindow.title('Timer lasera')

    #Set window to appear in the middle
    windowWidth = 330
    windowHeight = 122
    screenWidth = initialWindow.winfo_screenwidth()
    screenHeight = initialWindow.winfo_screenheight()

    x_pos = math.floor((screenWidth - windowWidth) / 2)
    y_pos = math.floor(((screenHeight - windowHeight) / 2) * 0.80)

    initialWindow.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")

    #NO button command
    def shortWindowHide():
        initialWindow.withdraw()
        time.sleep(2)  #2 minuty = 120
        initialWindow.deiconify()

    #YES button command
    def timerStart():
        initialWindow.withdraw()
        time.sleep(2) #1h = 3600
        createRecurringWindow()
        initialWindow.destroy()

    #Labels and Buttons for first window
    isLoggerOn = tk.Label(
        initialWindow,
        text = 'Czy włączono logger lasera?',
        width = 22,
        height = 2,
        font='Times 18 bold',
        padx=10,
        pady=10,
        justify='center'
        )
    isLoggerOn.pack()

    timerStartButton = tk.Button(
        initialWindow,
        text='TAK +1h',
        bg='light green',
        justify='center',
        font='Times 18 bold',
        command= timerStart
    )
    timerStartButton.pack(side='left', expand=True,fill=tk.BOTH)

    shortWindowHideButton = tk.Button(
        initialWindow,
        text='NIE +2 min',
        bg='red',
        font='Times 18 bold',
        command = shortWindowHide
    )
    shortWindowHideButton.pack(side='right', expand= True,fill=tk.BOTH)
    initialWindow.mainloop()


#second window creator 
def createRecurringWindow():
    recurringWindow = tk.Tk()
    recurringWindow.title('Timer lasera')

    #Set window to appear in the middle
    windowWidtg = 330
    windowHeight = 122
    screenWidth = recurringWindow.winfo_screenwidth()
    screenHeight = recurringWindow.winfo_screenheight()

    x_pos = math.floor((screenWidth - windowWidtg) / 2)
    y_pos = math.floor(((screenHeight - windowHeight) / 2) * 0.80)

    recurringWindow.geometry(f"{windowWidtg}x{windowHeight}+{x_pos}+{y_pos}")

#OK button command
    def timerRestart():
        recurringWindow.withdraw()
        time.sleep(2) #1h = 3600
        recurringWindow.deiconify()

#Label and Button for second window
    changeLog = tk.Label(
        recurringWindow,
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
    recurringWindow,
    text='OK',
    bg='light green',
    justify='center',
    font='Times 18 bold',
    command= timerRestart
    )
    yesButton2.pack(expand=True,fill=tk.BOTH)

#program start

time.sleep(2) #8 minut = 480 s

createInitialWindow()