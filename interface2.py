"""
BERTRAND Anthony

This file contains the structure of the vue.
"""

from tkinter import * 
import coderp


def geoliste(g):
    """return the geometry of a window g"""
    r=[i for i in range(0,len(g)) if not g[i].isdigit()]
    return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]

def popup(top):
    """create a popup window"""
    _,_,X,Y = geoliste(fenetre.geometry())
    top.resizable(width=False, height=False)
    top.geometry("300x400%+d%+d" % (X,Y))
    top.grab_set()
    top.transient(fenetre)
    fenetre.wait_window(top)

def charger():
    """load a language"""
    top = Toplevel(fenetre)
    popup(top)
    top.title("charger")


def creer():
    """create a new language"""
    top = Toplevel(fenetre)
    popup(top)
    top.title("creer")


def importer():
    """import a language from a file"""
    top = Toplevel(fenetre)
    popup(top)
    top.title("importer")


def exporter():
    """export a language in a file"""
    top = Toplevel(fenetre)
    popup(top)
    top.title("exporter")


def translate1():
    """translate from text to code"""
    text = text_crypt.get("1.0", "end-1c")
    print(text)
    text_crypt2.config(state=NORMAL)
    text_crypt2.delete(1.0,"end")
    text_crypt2.insert(1.0, hill.code(text, 0))
    text_crypt2.config(state=DISABLED)

def translate2():
    """translate from code to text"""
    text = text_decrypt.get("1.0", "end-1c")
    print(text)
    text_decrypt2.config(state=NORMAL)
    text_decrypt2.delete(1.0,"end")
    text_decrypt2.insert(1.0, hill.code(text, 1))
    text_decrypt2.config(state=DISABLED)

# initialise the Hill cipher
hill = coderp.Hill()

# Main window
fenetre = Tk()
fenetre.geometry('800x400')
fenetre.minsize(width=600, height=300)

# Menubar with the  4 new features
menu = Menu(fenetre)
menu.add_command(label="charger", command=charger)
menu.add_command(label="créer", command=creer)
menu.add_command(label="importer", command=importer)
menu.add_command(label="exporter", command=exporter)

# initialise my 2 main frames
crypt = Frame(fenetre, bg="green")
crypt.pack(side=TOP, expand=YES, fill=BOTH)
decrypt = Frame(fenetre, bg="yellow")
decrypt.pack(side=BOTTOM, expand=YES, fill=BOTH)

# content of the frame 1
crypt_var = StringVar()
text_crypt = Text(crypt, height=0, width=0)
text_crypt.pack(side=LEFT, expand=YES, fill=BOTH, padx=50, pady=20)
button_crypt = Button(crypt, text="Traduire", command=translate1)
button_crypt.pack(side=LEFT)
label_crypt_var = StringVar()
text_crypt2 = Text(crypt, height=0, width=0)
text_crypt2.pack(side=LEFT, expand=YES, fill=BOTH, padx=50, pady=20)

# content of the frame 2
decrypt_var = StringVar()
text_decrypt = Text(decrypt, height=0, width=0)
text_decrypt.pack(side=LEFT, expand=YES, fill=BOTH, padx=50, pady=20)
button_decrypt = Button(decrypt, text="Traduire", command=translate2)
button_decrypt.pack(side=LEFT)
text_decrypt2 = Text(decrypt, height=0, width=0)
text_decrypt2.pack(side=LEFT, expand=YES, fill=BOTH, padx=50, pady=20)

fenetre.config(menu=menu, bg="black")
fenetre.mainloop()