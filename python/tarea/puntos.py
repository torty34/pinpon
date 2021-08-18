import random
import math

def n_ale():
    file = open('prueba.txt','w')
    for i in range (100):
        file.write(str(random.randint(1,100 ))+'\n')
    file.close()
def leer():
    v={}
    i=0
    file = open ('prueba.txt')
    for linea in file:
        v[i]=int(linea)
        i+=1
    return v
def suma(a):
    s=0
    for i in a:
        s+=a[i]
    return s
def promedio(p,s):
    pro=s/len(p)
    return pro
def des(a,p):
    sh=0
    for i in range(len(a)):
        h=a[i]-p
        h=pow(h,2)
        h=pow(h,0.5)
        sh+=h
    v=sh/len(a)
    return v
n_ale()
#a=leer()    
#h=suma(a)
#poo=promedio(a,h)
#ds=des(a,poo)

#print(h,poo,ds)