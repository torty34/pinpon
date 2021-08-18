def men(ve):
    if len(ve)!=1:
        nv=[ [0 for columna in range(1)] for columna in range(len(ve)-1)]
        nn=[ [0 for columna in range(1)] for columna in range(len(ve))]
        f=0
        a=0#variable para identificar el mayor
        for i in range(len (ve)):    
            if ve[i]>a:#condicional mayor a menor
                a=ve[i]
        for j in range (len(ve)):
            if ve[j]!=a:
                nv[f]=ve[j] 
                f+=1
        nn[0]=a
        nv=men(nv)
        
        for k in range (len(nv)):
            nn[k+1]=nv[k]
        return  (nn)
    else:
        return (ve)        
d=3,2,1,7,9
print(men(d)) 
