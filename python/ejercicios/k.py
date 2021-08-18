def cambio (v1):
    v2 = [ [0 for columna in range(1)] for columna in range(len(v1))]
    for i in range (len(v1)):
        v2[i]=v1[i]
    return v2     

def ordenar(v1):
    v2 = [ [0 for columna in range(1)] for columna in range(len(v1))]
    for i in range(len(v1)-1):
        a=100
        for j in range (i,len(v1)):
            if v1[j]<a:
                a=v1[j]
        v2[i]=a
        b=i+1
        for k in range(i,len(v1)):
            if v1[k]!=a: 
                v2[b]=v1[k]
                b+=1
        v1=cambio(v2)
    print(v1)
v= 5,7,4,6,8,1,9,2,3
ordenar(v)