from tkinter import *
import math
import p
import puntos
f=10 
h=300
canvas = Canvas(width=1200, height=1000, bg='white')
canvas.pack(expand=YES, fill=BOTH)
matriz=p.imprimir()
#for i in range (99):
#    canvas.create_line(i*f,matriz[i][0]+h,(i+1)*f,matriz[i+1][0]+h,)
#    canvas.create_line(i*f,matriz[i][1]+h,(i+1)*f,matriz[i+1][1]+h,)
for i in range(99):
    x=matriz[i][0]
    y=matriz[i][1]
    #canvas.create_oval(i*f,yy,i*f,yy, fille='red')    
    canvas.create_oval((x*f)-3,(y*f)-3,(x*f)+3,(y*f)+3, )    

#file = open('prueba.txt')
#v={}
#i=0
#for linea in file:
#    v[i]=int(linea)
#    i+=1
#proy=1
#sumaa=puntos.suma(v)
#pro=puntos.promedio(v,sumaa)
#dess= puntos.des(v,pro)
#print(dess)
#canvas.create_line(0,pro+h,(1000),pro+h,fill='red')
#canvas.create_line(0, (pro+h)-dess,(1000), (pro+h)-dess,fill='blue')
#canvas.create_line(0, (pro+h)+dess,(1000), (pro+h)+dess,fill='blue')
#for j in range (1,100):
#    canvas.create_line(j*f,v[j]+h,j*f,v[j]+h)
#for i in range (1,99):
#    canvas.create_line(i*f,v[i]+h,(i+1)*f,v[i+1]+h,fill='orange')    
#
#file.close()
mainloop()