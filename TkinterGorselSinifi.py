from tkinter import *

class Arayuz(Tk):
    def __init__(self):
        Tk.__init__(self)
        pass
    
    def ekle(self,tip):
        self.element = tip().pack()
        pass
    
main = Arayuz()
main.ekle(Button)
