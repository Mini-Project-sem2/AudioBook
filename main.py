from tkinter import Tk
from tkinter.filedialog import askopenfilename

import PyPDF2
import pyttsx3

# GUI and get pdf
Tk().withdraw()
pdfLocation = askopenfilename()

# convert pdf to audiobook
book = open(pdfLocation, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
for i in range(0, pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    newVoiceRate = 145
    speaker.setProperty('rate', newVoiceRate)
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
