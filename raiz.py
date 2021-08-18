from tkinter import *
from tkinter.ttk import *
from mobb import *

to = Tk()
to.config(bg='#100010')
#teclas usadas
def teclado(b,obj,a):
    if __name__ == "__main__":

        circulo = Kilo(b,obj)
        a.bind("<KeyPress-o>", lambda e: circulo.o(e))
        a.bind("<KeyPress-Left>", lambda e: circulo.left(e))
        a.bind("<KeyPress-Right>", lambda e: circulo.right(e))
        a.bind("<KeyPress-Up>", lambda e: circulo.up(e))
        a.bind("<KeyPress-Down>", lambda e: circulo.down(e))

toto = Canvas(to,width=1000,height=500,bg='#000')
toto.pack(fill = 'none', expand='True')
re =[0, 0, 20, 20, '#f0f000']
teclado(toto,re,to)
to.mainloop()
