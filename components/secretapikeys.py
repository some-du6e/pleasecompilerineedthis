# hi
chance=0.5
no = "components/topsecret/talking-ben-no.mp3"
yes = "components/topsecret/talking-benn-yes.mp3"
laugh = "components/topsecret/talking-benny-laugh.mp3"
anderdingus = "components/topsecret/anderdingus.mp3"

from tkinter import ttk

import playsound
import random
import time
import tkinter as tk
import components.evaluator as evaluator
def sensitiveFunction(fast=False, line="log('hi')", filename="not defined!"):
    root = tk.Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    # use a regular tk.Label so foreground changes reliably
    color = "#000000"
    label = tk.Label(frm, text=line, font=("Arial", 121), fg=color, bg=root.cget("bg"))
    label.grid(column=0, row=0)
    # good enough window centering
    root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
    root.update()
    time.sleep(1)
    if random.random() < chance:
        root.update() # render it cuz im dumb
        # play the sound
        playsound.playsound(yes, block=not fast)
        # anderdingussing
        if "anderdingus" in line.lower():
            playsound.playsound(anderdingus, block=False)
        # get compiled line
        compiledline = evaluator.plstopythonfr(line, filename, fast)
        # change text to compiled line
        label.config(text=compiledline)
        root.update() # render it cuz im dumb
        # change text color
        label.config(fg="#00FF00", bg="white")
        root.update() # render it cuz im dumb
        root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id())) # center it again cuz of the text that changed
        root.update() # render it cuz im dumb
        if fast: time.sleep(1.15)
        if "anderdingus" in line.lower(): time.sleep(2) # wait for the anderdingus to finish
        root.destroy() # kill after allat
        return compiledline
    else:
        root.update() # render it cuz im dumb
        # change text color
        label.config(fg="#FF0000", bg="white")
        root.update() # im dumb
        # play the sound
        selectedsound = random.choice([no, laugh])
        playsound.playsound(selectedsound, block=not fast)
        
        
        if fast: time.sleep(1)
        root.destroy() # kill after allat
        return "print(Exception('No thanks'))"