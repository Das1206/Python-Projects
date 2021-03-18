#!/usr/bin/env python
# coding: utf-8

# # Converting text to speech using python

# In[9]:


# We are going to be using gtts module which is a tool to interface with google text tp speech API
# You will need to install gtts module before importing
from gtts import gTTS
import os 
from tkinter import *


# In[13]:


root = Tk()
canvas = Canvas(root, width = 400, height = 300 )
canvas.pack()

# Our text to speech converter function 
def texttospeech():
    text= entry.get()
    language = 'en'
    output = gTTS(text = text, lang = language,slow =False )
    output.save('Output.mp3')
    os.system('Start Output.mp3')

entry =  Entry(root)
canvas.create_window(200,100, window = entry)

# Now lets create a button that needs to be clicked for translation
button = Button(text = 'Start', command = texttospeech)
canvas.create_window(200,300, window = button)

# packing all our tkinter elements
root.mainloop()

