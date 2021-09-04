import win32api, win32con, time, keyboard, random, threading, tkinter as tk
from tkinter import *


###
version = '1.0'

window = tk.Tk()
window.title(f'BM [v.{version}]')
window.geometry('240x345')
#window.iconbitmap('content\image.ico')
window.resizable(False, False)
frame = Frame(window, padx=10, pady=5)
###


###
def BM_MainWindow():
    frame.grid(row=0, column=0)

    for i in range(9):
        buttonList[i].grid(row=i, column=0, pady=2)

    for i in range(9):
        scaleList[i].grid(row=i, column=1, padx=5)

    for i in range(9):
        entryList[i].grid(row=i, column=2, padx=5)
###


###
def EntryUpdater(value):
    for i in range(9):
        entryList[i].delete(0, 'end')
        entryList[i].insert(0, str(scaleList[i].get()))

def ButtonManager(i):
    window.focus()
    if buttonStateList[i] == False:
        buttonStateList[i] = True
        buttonList[i].config(bg='SpringGreen2')
        scaleList[i].config(state='normal')
        entryList[i].config(state='normal')
        entryList[i].delete(0, 'end')
        entryList[i].insert(0, '1')
    else:
        buttonStateList[i] = False
        buttonList[i].config(bg='SystemButtonFace')
        scaleList[i].set(1)
        scaleList[i].config(state='disabled')
        entryList[i].delete(0, 'end')
        entryList[i].insert(0, '1')
        entryList[i].config(state='readonly')
def varUpdater(i):
    global keysList
    #if not True in buttonStateList:
    keysList = []

    var = stringvarList[i].get()
    if var != '' and True in buttonStateList:
        scaleList[i].set(var)

        for i in range(9):
            if buttonStateList[i] == True:
                for i1 in range(int(stringvarList[i].get())):
                        keysList.append(buttonList[i].cget("text"))
###


###
def BlockMixer():

    while True:
        if win32api.GetAsyncKeyState(win32con.VK_RBUTTON) != False and keysList != []:
            time.sleep(0.2)
            button = str(random.choice(keysList))
            keyboard.send(f'{button}')

        time.sleep(0.1)
threading.Thread(target=BlockMixer).start()
###


###
keysList = []

buttonList = []
buttonStateList = []
for i in range(9):
    buttonList.append(Button(frame, width=3, font=('Consolas'), relief=GROOVE, borderwidth=2, text=str(i+1), command=lambda c=i: ButtonManager(int(buttonList[c].cget("text"))-1)))
    buttonStateList.append(False)
    

scaleList = []
for i in range(9):
    scaleList.append(Scale(frame, width=20, length=140, from_=1, to=10, orient=HORIZONTAL, showvalue=False, command=EntryUpdater, state='disabled'))

stringvarList = []
for i in range(9):
    stringvarList.append(StringVar())
    stringvarList[i].trace("w", lambda  name, index, mode, sv=stringvarList[i], c=i,: varUpdater(c))

entryList = []
for i in range(9):
    entryList.append(Entry(frame, width=3, relief=GROOVE, borderwidth=2, justify=CENTER, textvariable=stringvarList[i]))
    entryList[i].insert(0, '1')
    entryList[i].config(state='readonly')
###

BM_MainWindow()
window.mainloop()