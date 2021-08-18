import poligonos
from tkinter import *
import math
canvas = Canvas(width=1000, height=1000, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(10, 10, 80, 80,)
canvas.create_line(10, 80, 80, 10,)
f=100
h=1
g='hola'
for i in range (500):
    x=i*10
    y=(math.sin(x)*10)+100
    canvas.create_line(x,y,x,y, width=1, fill='white' )


coordenadas= [2,3,4,2,6,6,5,2,2,2]
punto=[1,3]
canvas.create_oval((punto[0]*f)-h,(punto[1]*f)-h , (punto[0]*f)+h, (punto[1]*f)+h,)
g=poligonos.ecuacion(coordenadas,punto)
canvas.create_text(100, 10, text=g, fill='black')

i=0
t=len(coordenadas)

while i<=(t//2):
    j=i*2
    x1=coordenadas[j%t]*f
    y1=coordenadas[(j+1)%t]*f
    x2=coordenadas[(j+2)%t]*f
    y2=coordenadas[(j+3)%t]*f
    canvas.create_line(x1,y1,x2,y2,)
    i+=1
mainloop()