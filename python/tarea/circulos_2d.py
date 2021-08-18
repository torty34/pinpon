import math
import cordenadas
def comparacion(a,b):
    
    k=(b[0])-(a[0])
    c=(b[1])-(a[1])
    r=(b[2])+(a[2])
    if k==0 and c==0 :
        z=('si chocan')    
    elif k==0 :
        if c<0:
            c*=-1
        if c>r :
            z=('no chocan')
        else:
            z=('si chocan')    
    elif c==0 :
        if k<0:
            k*=-1
        if k>r :
            z=('no chocan')
        else:
            z=('si chocan')    
    else :
        x= pow(k,2)
        y= pow(c,2)
        xy= x+y
        cc=pow(xy,0.5)
        if cc>r:
            z=('no chocan')
        else:
            z=('si chocan')
    return z                
a=cordenadas.ints()
b=cordenadas.ints()
print(comparacion(a,b))
