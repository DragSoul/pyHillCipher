"""
BERTRAND Anthony

This file contains the structure of the vue.
"""

from os import name
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.font import BOLD
from writefile import read_file
from writefile import add_language
import random as rd
import coderp

#------------------------------------------------------------------------------
def geoliste(g):
    """return the geometry of a window g"""

    r=[i for i in range(0,len(g)) if not g[i].isdigit()]
    return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]

#------------------------------------------------------------------------------
def popup(top):
    """create a popup window"""
    
    top.resizable(width=False, height=False)
    
    top.grab_set()
    top.transient(fenetre)
    
#------------------------------------------------------------------------------
def charger():
    """load a language"""
    
    #--------------------------------------------------------------------------
    def select(event):
        """Select the language"""

        print(combobox.get())
        for language in languages:
            name, a, b, c, d = language
            if name == combobox.get():
                msg = hill.check_matrix(a, b, c, d)
                print(msg)
                

    
    top = Toplevel(fenetre)
    popup(top)
    _,_,X,Y = geoliste(fenetre.geometry())
    top.geometry("150x200%+d%+d" % (X,Y))
    top.title("charger")

    languageSelect	= StringVar()
    languages = read_file("languages.txt")
    languages_name = []
    for language in languages:
        languages_name.append(language[0])

    combobox = Combobox(top, textvariable=languageSelect, values=languages_name, \
        state='readonly')
    combobox.bind('<<ComboboxSelected>>', func=select)
    combobox.pack()
    


    

#------------------------------------------------------------------------------
def creer():
    """create a new language"""

    #--------------------------------------------------------------------------
    def auto_hill():
        '''take random numbers that fit the conditions of the Hill cypher.
        The tuple can't be the same as another one in the file.'''
        languages = read_file("languages.txt")

        # Check for name first
        languages_name = []
        for language in languages:
            languages_name.append(language[0])
        name = entry_name.get()
        if(name in languages_name or name == '' or ' ' in name):
            print("pb")
        else : print("ok")

        # loop until we found a good tuple.
        boolean = True
        while boolean:
            a = rd.randint(1, 100)
            b = rd.randint(1, 100)
            c = rd.randint(1, 100)
            d = rd.randint(1, 100)
            msg = hill.check_matrix(a, b, c, d)
            if msg == 'valide':
                print('valide')
                # now we must check the existence of this tuple in our file
                exist = False
                for language in languages:
                    _, fa, fb, fc, fd = language
                    if (a, b, c, d) == (fa, fb, fc, fd):
                        exist = True
                        break
                if exist == True:
                    continue
                else:
                    boolean = False
                    s = name + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d)
                    add_language('languages.txt', s)



    top = Toplevel(fenetre)
    popup(top)
    _,_,X,Y = geoliste(fenetre.geometry())
    top.geometry("300x400%+d%+d" % (X,Y))
    top.title("créer")

    # First frame : name of the language
    frame1 = Frame(top)
    frame1.pack(expand=False, fill=BOTH)
    label_name = Label(frame1, text="Choisir un nom :", font=("Arial", 14))
    label_name.pack()
    entry_name = Entry(frame1)
    entry_name.pack()

    # separator line
    canvas = Canvas(top, height=10)
    canvas.pack(expand=False, fill=BOTH)
    canvas.create_line(0,10,300,10,fill="black", width=2)

    # Second frame : explanation
    frame2 = Frame(top)
    frame2.pack(expand=False, fill=BOTH, pady=10)
    label_frame2 = Label(frame2, text="Création manuelle", font=("Arial", 18))
    label_frame2.pack()
    label_frame2 = Label(frame2, text="Choisissez 4 nombres a, b, c, d tel que\
 a*d - b*c soit premier avec 26", font=("Arial", 12), wraplength=300)
    label_frame2.pack()

    # Third frame : manual selection
    frame3 = Frame(top)
    frame3.pack(expand=False, fill=BOTH)

    frame_a = Frame(frame3)
    frame_a.grid(row=0, column=1)
    label_a = Label(frame_a, text="a = ", font=("Arial", 14))
    label_a.pack(side=LEFT)
    entry_a = Entry(frame_a, width=4)
    entry_a.pack(side=LEFT)

    frame_b = Frame(frame3)
    frame_b.grid(row=0, column=2)
    label_b = Label(frame_b, text="b = ", font=("Arial", 14))
    label_b.pack(side=LEFT)
    entry_b = Entry(frame_b, width=4)
    entry_b.pack(side=LEFT)

    frame_c = Frame(frame3)
    frame_c.grid(row=1, column=2)
    label_c = Label(frame_c, text="c = ", font=("Arial", 14))
    label_c.pack(side=LEFT)
    entry_c = Entry(frame_c, width=4)
    entry_c.pack(side=LEFT)

    frame_d = Frame(frame3)
    frame_d.grid(row=1, column=1)
    label_d = Label(frame_d, text="d = ", font=("Arial", 14))
    label_d.pack(side=LEFT)
    entry_d = Entry(frame_d, width=4)
    entry_d.pack(side=LEFT)

    button_test = Button(frame3, text="Test")
    button_test.grid(column=1, row=2, pady=10)
    button_valid = Button(frame3, text="Valider")
    button_valid.grid(column=2, row=2)

    # set a minimal column size to center the content
    col_count, row_count = frame3.grid_size()
    for col in range(col_count):
        frame3.grid_columnconfigure(col, minsize=300/4)

    for row in range(row_count):
        frame3.grid_rowconfigure(row, minsize=20)

    # separator line
    canvas = Canvas(top, height=10)
    canvas.pack(expand=False, fill=BOTH)
    canvas.create_line(0,10,300,10,fill="black", width=2)

    # Forth and last frame : magical button
    frame4 = Frame(top)
    frame4.pack(expand=False, fill=BOTH, pady=10)
    label_frame4 = Label(frame4, text="Création automatique", font=("Arial", 18))
    label_frame4.pack()
    magic_button = Button(frame4, text="Bouton magique !", font=("Arial", 14),\
        command=auto_hill, height=10)
    magic_button.pack(pady=10)

    

#------------------------------------------------------------------------------
def importer():
    """import a language from a file"""

    top = Toplevel(fenetre)
    popup(top)
    top.title("importer")

#------------------------------------------------------------------------------
def exporter():
    """export a language in a file"""

    top = Toplevel(fenetre)
    popup(top)
    top.title("exporter")

#------------------------------------------------------------------------------
def translate1():
    """translate from text to code"""

    text = text_crypt.get("1.0", "end-1c")
    text_crypt2.config(state=NORMAL)
    text_crypt2.delete(1.0,"end")
    text_crypt2.insert(1.0, hill.code(text, 0))
    fenetre.clipboard_clear()                      # Copy the result in the clipboard 
    fenetre.clipboard_append(hill.code(text, 0))   # to avoid the pb of the textarea disabled
    text_crypt2.config(state=DISABLED)

#------------------------------------------------------------------------------
def translate2():
    """translate from code to text"""

    text = text_decrypt.get("1.0", "end-1c")
    text_decrypt2.config(state=NORMAL)
    text_decrypt2.delete(1.0,"end")
    text_decrypt2.insert(1.0, hill.code(text, 1))
    fenetre.clipboard_clear()
    fenetre.clipboard_append(hill.code(text, 1))
    text_decrypt2.config(state=DISABLED)



#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


# initialise the Hill cipher
hill = coderp.Hill()

# Main window
fenetre = Tk()
fenetre.geometry('800x400')
fenetre.minsize(width=600, height=300)

# Menubar with the  4 new features
menu = Menu(fenetre, bg="CornflowerBlue", activebackground="DeepSkyBlue")
menu.add_command(label="charger", command=charger)
menu.add_command(label="créer", command=creer)
menu.add_command(label="importer", command=importer)
menu.add_command(label="exporter", command=exporter)

# initialise my 2 main frames
crypt = Frame(fenetre, bg="blue")
crypt.pack(expand=YES, fill=BOTH)
decrypt = Frame(fenetre, bg="darkblue")
decrypt.pack(side=BOTTOM, expand=YES, fill=BOTH)

# content of the frame 1
label_crypt = Label(crypt, text="Coder", bg="blue", font=("Arial", 16, BOLD), fg="DeepSkyBlue")
label_crypt.pack()
crypt_var = StringVar()
text_crypt = Text(crypt, height=0, width=0, bg="lightblue", border=0, exportselection=1)
text_crypt.pack(side=LEFT, expand=YES, fill=BOTH, padx=50, pady=20)
button_crypt = Button(crypt, text="Traduire", bg="CornflowerBlue", activebackground="DeepSkyBlue", border=0, command=translate1)
button_crypt.pack(side=LEFT)
label_crypt_var = StringVar()
text_crypt2 = Text(crypt, height=0, width=0, bg="lightblue", border=0, state=DISABLED)
text_crypt2.pack(side=LEFT, expand=YES, fill=BOTH, padx=50, pady=20)

# content of the frame 2
label_decrypt = Label(decrypt, text="Décoder", bg="darkblue",font=("Arial", 16, BOLD), fg="DeepSkyBlue")
label_decrypt.pack()
decrypt_var = StringVar()
text_decrypt = Text(decrypt, height=0, width=0, bg="lightblue", border=0, exportselection=1)
text_decrypt.pack(side=LEFT, expand=YES, fill=BOTH, padx=50, pady=20)
button_decrypt = Button(decrypt, text="Traduire", bg="CornflowerBlue", activebackground="DeepSkyBlue", border=0, command=translate2)
button_decrypt.pack(side=LEFT)
text_decrypt2 = Text(decrypt, height=0, width=0, bg="lightblue", border=0, state=DISABLED)
text_decrypt2.pack(side=LEFT, expand=YES, fill=BOTH, padx=50, pady=20)

fenetre.config(menu=menu, bg="black")
fenetre.mainloop()