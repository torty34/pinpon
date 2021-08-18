import cordenadas
from tkinter import*
canvas = Canvas(width=1000, height=1000, bg='white')
canvas.pack(expand=YES, fill=BOTH)
e=7#expancion en la grafica
def ovalo(ovalo):
    x=ovalo[0]
    y=ovalo[1]
    r=ovalo[2]
    canvas.create_oval((x*e)-r,(y*r)+r,(x*r)+r,(y*r)-r,fill='red' )    
def cor():
    oval1=cordenadas.ints()
    oval2=cordenadas.ints()
    ovalo(oval1)
    ovalo(oval2)
def manteca():
    v=34,58
    r=10#radio
    x=v[0]
    y=v[1]
    canvas.create_oval((x*e)-r,(y*e)-r,(x*e)+r,(y*e)+r)

manteca()
mainloop()