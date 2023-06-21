import tkinter as tk
import time
import math

# program config (in seconds):
# time before first window pop's out
programInitialDelay = 480
# time before first window pop's out again after clicking NO
shortHideButtonDelay = 120
# !!!CHANGE NOT ADVISED!!! time before "change log file" info pop's out again
timerDelay = 3600

# GUI and commands code


def createWindow():
    window = tk.Tk()
    window.title("Timer lasera")

    windowWidth = 330
    windowHeight = 122
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    x_pos = math.floor((screenWidth - windowWidth) / 2)
    y_pos = math.floor(
        ((screenHeight - windowHeight) / 2) * 0.80)  # multiply by 0.8
    # to make the window appear more to the top of the screen

    window.geometry(f"{windowWidth}x{windowHeight}+{x_pos}+{y_pos}")
    return window


def createLabel(window, text):
    label = tk.Label(
        window,
        text=text,
        width=22,
        height=2,
        font='Times 18 bold',
        padx=10,
        pady=10,
        justify='center')
    return label


def createButton(window, buttonText, bgColor, buttonCommand):
    button = tk.Button(
        window,
        text=buttonText,
        bg=bgColor,
        justify='center',
        font='Times 18 bold',
        command=buttonCommand)
    return button


# first window creator
def createInitialWindow():
    initialWindow = createWindow()

    # NO button command
    def shortWindowHide():
        initialWindow.withdraw()
        time.sleep(shortHideButtonDelay)
        initialWindow.deiconify()

    # YES button command
    def timerStart():
        initialWindow.withdraw()
        time.sleep(timerDelay)
        createRecurringWindow()
        initialWindow.destroy()

    # Labels and Buttons for first window
    isLoggerOn = createLabel(initialWindow, "Czy włączono logger lasera?")
    isLoggerOn.pack()

    timerStartButton = createButton(
        initialWindow, "TAK +{time}h".format(time=round(
            (timerDelay/3600))), 'light green', timerStart)
    timerStartButton.pack(side='left', expand=True, fill=tk.BOTH)

    shortWindowHideButton = createButton(
        initialWindow, "NIE +{time}min".format(time=round(
            (shortHideButtonDelay/60))), 'red', shortWindowHide)
    shortWindowHideButton.pack(side='right', expand=True, fill=tk.BOTH)
    initialWindow.mainloop()


# second window creator
def createRecurringWindow():
    recurringWindow = createWindow()

    # OK button command
    def timerRestart():
        recurringWindow.withdraw()
        time.sleep(timerDelay)
        recurringWindow.deiconify()

    # Label and Button for second window
    changeLog = createLabel(
        recurringWindow, "ZMIEŃ LOG LASERA \n(nie nad linią!)")
    changeLog.pack()

    timerRestartButton = createButton(
        recurringWindow, 'OK', 'light green', timerRestart)
    timerRestartButton.pack(expand=True, fill=tk.BOTH)


# program start
time.sleep(programInitialDelay)
createInitialWindow()
