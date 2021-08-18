#f=input()+','
def ints(f):
    j=0
    nv = {}
    h=0
    cs=1
    for i in range (len(f)):
        if f[i]=='-':
           cs=-1
        if f[i].isdigit() :
           h=h*10+(int(f[i]))   
           if (i<len(f) and (f[i+1].isdigit())== False) : 
               nv[j]=h*cs
               #print(nv[j], type(nv[j]),j)
               j+=1 
               h=0              
               cs=1
    return nv     
#a=input()+','
#a=ints(a)
#imprimir(a)
