# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 22:04:47 2018

@author: RAVI
"""

from tkinter import *
from tkinter.ttk import *
#import POS.integrateGetPOS as ip
#import ValenceCollapse.computeValence as cv
from BOW.Get_bow_politeness import getPoliteness
from BOW.Get_bow_politeness import calc
import ValenceCollapse.computeValence as vp
import POS.integrateGetPOS as pos
class Polite:
    def __init__(self, root):
        root.title("Po-Lite")
        f = Frame(root)
        #f.config(width=1000,height=500)
        f.grid()

        widget = Label(root,text='Politeness Detection')
        labelfont1 = ('Monotype Corsiva', 25, 'bold')
        widget.config(font=labelfont1)
        widget.grid(row=0, column=0)
        labelfont = ('Segoe Print', 10, 'bold')

        entertxt = Label(root, text='Enter Text')
        entertxt.config(font=labelfont)
        entertxt.grid(row=11, column=0, pady=10, padx=10, sticky=W)

        mystring = StringVar()

        def getvalue():
            input_text = mystring.get()
            #cv.computePolitenessbyValence(s)
            getPoliteness(input_text)
            val1 = vp.computePolitenessbyValence(input_text)
            val = calc(input_text)
            bow(val)
            valence(val1)
            strin = pos.getPOSpoliteness(input_text)
            post(strin)
            #valence(val)
            
        name=Entry(root, textvariable=mystring,width=70)
        name.grid(row=12, column=0, sticky=W)  # entry textbox
        Button(root, text="OK", command=getvalue).grid(row=14, column=0, sticky=W)  # button
        
        def clear():
            name.delete(0, END)
            
        Button(root, text='CLEAR', command=clear).grid(row=14, column=1, pady=10, padx=10, sticky=W)
        def bow(val):
            polit = Label(root, text='BOW')
            polit.config(font=labelfont)
            polit.grid(row=10, column=10, pady=10, padx=10, sticky=W)
    
            progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
            progress['value'] = val
            progress.grid(row=11, column=10, pady=10, padx=10, sticky=W)

            polit = Label(root, text= val)
            polit.config(font=labelfont)
            polit.grid(row=12, column=10, pady=1, padx=1, sticky=W)
                        
            
        def valence(val1):
            bag = Label(root, text='Valence Collapse')
            bag.config(font=labelfont)
            bag.grid(row=10, column=11, pady=10, padx=10, sticky=W)
    
            progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
            progress['value'] = val1
            progress.grid(row=11, column=11, pady=10, padx=10, sticky=W)
    
            bag = Label(root, text= val1)
            bag.config(font=labelfont)
            bag.grid(row=12, column=11, pady=10, padx=10, sticky=W)
            
        def post(strin):
            bag = Label(root, text='POS Politeness  ---> ')
            bag.config(font=labelfont)
            bag.grid(row=14, column=10, pady=10, padx=10, sticky=W)
    
            bag = Label(root, text= strin)
            bag.config(font=labelfont)
            bag.grid(row=14, column=11, pady=10, padx=10, sticky=W)

# Main
root = Tk()
obj=Polite(root) #object instantiated
root.mainloop()