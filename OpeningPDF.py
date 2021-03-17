from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3
#import pathlib

root=Tk()
root.geometry('500x500')
my_menu=Menu(root)
root.config (menu=my_menu, bg="#d8fefe")
text_box=Text(root, height=30, width=50)
text_box.pack(pady=8)

def openfile():
    open_my_pdf=filedialog.askopenfilename(initialdir= 'opening PDF/pdfs',title='Abrir archivos PDF:',
                                         filetype=(('Solo pdf','*.pdf'),('Cualquier archivo','*.*')))
    if open_my_pdf:
        pdf_selected=PyPDF2.PdfFileReader(open_my_pdf)
        first_page= pdf_selected.getPage(1)
        the_text=first_page.extractText()
        text_box.insert(1.0, the_text)

        engine=pyttsx3.init()
        '''solo hay dos voces. Las dos en ingles Americano.
        voices=engine.getProperty('voices')
        for voice in voices:
            print('Voice:')
            print('id: '+voice.id)
            print('name: '+voice.name)
            print ('languages: %s'%voice.languages)
            print('gender: %s '%voice.gender)'''
            
        engine.say(the_text)
        engine.runAndWait()

def cancelcontent():
    
    text_box.delete(1.0, END)

file_menu= Menu (my_menu, tearoff='False')
my_menu.add_cascade(label='Fichero', menu=file_menu)
file_menu.add_cascade(label='Abrir', command=openfile)
file_menu.add_cascade(label='Borrar', command=cancelcontent)
file_menu.add_separator
file_menu.add_cascade(label='Salir', command=root.destroy)

root.mainloop()
