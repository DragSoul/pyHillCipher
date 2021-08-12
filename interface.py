"""
BERTRAND Anthony

This file contains the structure of the vue.
"""

from tkinter import * 
import coderp

class App:
    """Root of the vue, containing Chiffr and Dechiffr."""
    hill = None
    
    def __init__(self, master):
        self.hill = coderp.Hill()
        titre = Label(master, text="Traducteur")
        titre.pack()
        c = Chiffr(master, self.hill)
        d = Dechiffr(master, self.hill)


#------------------------------------------------------------------------------
class Chiffr:
    
    hill=None
    frame=None
    entree=None
    button=None
    label=None
    v=None
    a=None
    b=None
    c=None
    d=None

    #--------------------------------------------------------------------------
    def __init__(self, master, hill): 
        self.hill = hill
        self.frame = Frame(master, bg="yellow")
        self.frame.pack()
        
        titre = Label(self.frame, text="français -> encrypt")
        titre.pack()
        self.ver = StringVar()
        p3 = PanedWindow(self.frame, orient=VERTICAL, background="red")
        p1 = PanedWindow(p3, orient=HORIZONTAL)
        p2 = PanedWindow(p3, orient=HORIZONTAL)
        self.a = Entry(p1, width=4)
        self.b = Entry(p1, width=4)
        self.c = Entry(p2, width=4)
        self.d = Entry(p2, width=4)
        btnverif = Button(p3, text="test", command=self.verif)
        textverif = Label(p3, textvariable = self.ver)
        
        p1.add(self.a)
        p1.add(self.b)
        p2.add(self.c)
        p2.add(self.d)
        p3.add(p1)
        p3.add(p2)
        p3.add(btnverif)
        p3.add(textverif)
        
        p3.pack(side=LEFT)
        
        self.entree = Entry(self.frame)
        self.entree.pack(side=LEFT)
        
        self.button = Button(self.frame, text="trad", command=self.chif)
        self.button.pack(side=LEFT)
        
        self.v = StringVar()
        self.label = Label(self.frame, textvariable=self.v, wraplength=120,
                            width=20, height=5)
        self.label.pack(side=LEFT)
        
        btncopie = Button(self.frame, text="copie", command=self.copie)
        btncopie.pack(side=LEFT)
    
        #----------------------------------------------------------------------
    def copie(self):
        self.frame.clipboard_clear()
        self.frame.clipboard_append(self.label.cget("text"))

    #--------------------------------------------------------------------------     
    def chif(self):
        self.v.set(self.hill.code(self.entree.get(), 0))

    #--------------------------------------------------------------------------
    def verif(self):
        self.ver.set(self.hill.check_matrix(self.a.get(), self.b.get(),
                    self.c.get(), self.d.get()))
        

#------------------------------------------------------------------------------   
class Dechiffr:
    hill=None
    frame=None
    v=None
    entree=None
    button=None
    label=None
    a=None
    b=None
    c=None
    d=None
    
    #--------------------------------------------------------------------------   
    def __init__(self, master, hill):
        self.hill = hill
        self.frame = Frame(master, bg="green")
        self.frame.pack()
        
        titre = Label(self.frame, text="encrypt -> français")
        titre.pack()
        
        #
        self.ver = StringVar()
        p3 = PanedWindow(self.frame, orient=VERTICAL, background="red")
        p1 = PanedWindow(p3, orient=HORIZONTAL)
        p2 = PanedWindow(p3, orient=HORIZONTAL)
        p4 = PanedWindow(p3, orient=HORIZONTAL)
        self.a = Entry(p1, width=4)
        self.b = Entry(p1, width=4)
        self.c = Entry(p2, width=4)
        self.d = Entry(p2, width=4)
        btnget = Button(p4, text="get", command=self.verif)
        btnset = Button(p4, text="set", command=self.setmat)
        textverif = Label(p3, textvariable = self.ver)
        
        p1.add(self.a)
        p1.add(self.b)
        p2.add(self.c)
        p2.add(self.d)
        p3.add(p1)
        p3.add(p2)
        p4.add(btnget)
        p4.add(btnset)
        p3.add(p4)
        p3.add(textverif)

        
        p3.pack(side=LEFT)
        #
        
        self.entree = Entry(self.frame)
        self.entree.pack(side=LEFT)
        
        self.button = Button(self.frame, text="trad", command=self.dechif)
        self.button.pack(side=LEFT)
        
        self.v = StringVar()
        self.label = Label(self.frame, textvariable=self.v, wraplength=120,
                            height=5, width=20)
        self.label.pack(side=LEFT)
    
        btncopie = Button(self.frame, text="copie", command=self.copie)
        btncopie.pack(side=LEFT)

    #--------------------------------------------------------------------------
    def copie(self):
        self.frame.clipboard_clear()
        self.frame.clipboard_append(self.label.cget("text"))

    #--------------------------------------------------------------------------              
    def dechif(self):
        self.v.set(self.hill.code(self.entree.get(), 1))

    #--------------------------------------------------------------------------    
    def verif(self):
        self.a.delete(0, len(self.a.get()))
        self.a.insert(0, self.hill.decrypt[0][0])
        self.b.delete(0, len(self.b.get()))
        self.b.insert(0, self.hill.decrypt[0][1])
        self.c.delete(0, len(self.c.get()))
        self.c.insert(0, self.hill.decrypt[1][0])
        self.d.delete(0, len(self.d.get()))
        self.d.insert(0, self.hill.decrypt[1][1])

    #--------------------------------------------------------------------------     
    def setmat(self):
        a=int(self.a.get())
        b=int(self.b.get())
        c=int(self.c.get())
        d=int(self.d.get())
        if self.hill.gcd(a*d - b*c, 26) != 1:
            self.ver.set("erreur")
            return
        self.hill.decrypt[0][0] = a
        self.hill.decrypt[0][1] = b
        self.hill.decrypt[1][0] = c
        self.hill.decrypt[1][1] = d
        self.ver.set("ok")
        
        
# root = Tk()
# titre = Label(root, text="Traducteur").pack()
# titre1 = Label(root, text="Français -> encrypt").pack()
# a = Chiffr(root)
# titre2 = Label(root, text="encrypt -> Français").pack()
# b = Dechiffr(root)
# root.mainloop()

root = Tk()
a = App(root)
root.mainloop()
