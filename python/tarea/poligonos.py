import cordenadas
def comparacion(xx,yy,xxx,yyy,x,y,a,b):
    #print('h')        
    cero=0
    s=(yyy)-(yy)
    d=(xxx)-(xx)
    j=(a)-(xx)
    e= (b)-(yy)
    f= (x)-(xx)
    m=s/d  
    si = (-1)*m*(j)+(e)
    sii = (-1)*m*(x-(xx))+(y-(yy))
    #print(si,sii)
    if si>0:
        si=1
    else:
        si=0
    if sii>0:
        cero=0
        sii=1
    elif sii==0.0:
         cero=1
    else:
        cero=0
        sii=0
    if si==sii or cero==1 :
        h=1
    else:
        h=0
    return h                        
def ecuacion(ec,p): 
    yes=1
    k=0
    v=0
    print(p,ec)
    for i in range (0,len(ec)-1,2):  
        if i==0:
            e=4
            g=5
        else:
            e=0
            g=1
        if i+2==(len(ec)):
            v= comparacion(ec[i],ec[(i+1)],ec[e],ec[g],p[0],p[1],ec[i-2],ec[i-1])        
        else:
            v= comparacion(ec[(i)],ec[(i+1)],ec[(i+2)],ec[(i+3)],p[0],p[1],ec[e],ec[g])
        k+=v        
    if k==(len(ec)//2):
        return(1)
        #yes=int(input('1)desea comparar otro punto'))
    else :
        return(0)    
        #yes=int(input('1)desea comparar otro punto'))
def rango(o):
    cordenada=[40,40,70,70,80,60]
    punto=o
    ty=ecuacion(cordenada,punto)
    return ty
#rango()
#cordenada=input()+','
#punto= input()+','
#punto= cordenadas.ints(punto)
#cordenada=cordenadas.ints(cordenada)
#cordenadas.imprimir(cordenada)