from tkinter import*
canvas = Canvas(width=1000, height=1000, bg='white')
canvas.pack(expand=YES, fill=BOTH)
import poligonos
import nro
e=7
def dentro(mrt):
    mat = [ [0 for columna in range(3)] for columna in range(100)]
    for i in range(len(mrt)):
        for j in range(2):
            mat[i][j]=mrt[i][j]
        vec={}
        vec=mrt[i]
        #print(vec)
        tu=0
        tu=(poligonos.rango(vec))
        if tu==1: 
            mat[i][2]=1
        else:
            mat[i][2]==0
    return mat    
def graf_puntos(mtr):
    for i in range(len(mtr)):
        v=mtr[i]
        if v[2]==1:
            color='red'
        else:
            color='black'
        r=10#radio
        x=v[1]
        y=v[0]
        canvas.create_oval((x*e)-r,(y*e)-r,(x*e)+r,(y*e)+r,fill=color)
def graf_pol():
    f=e
    coordenadas=40,40,70,70,60,80
    t=6
    i=0
    while i <= (t//2) :
        z= i*2
        x1=coordenadas[z%t]*f
        y1=coordenadas[(z+1)%t]*f
        x2=coordenadas[(z+2)%t]*f
        y2=coordenadas[(z+3)%t]*f
        canvas.create_line(x1,y1,x2,y2,)
        i+=1
#nro.nroa()
h=nro.imprimir()
h=dentro(h)
#poligonos.rango(h)
graf_puntos(h)
graf_pol()
mainloop()