import cordenadas
def comparacion( a, b):
   k= 0  
      
   for i in range (0,4,2) :
       if a[i] < (a[i]+a[i+1]) :
           if (a[i] <= b[i] <= (a[i]+a[i+1]) ) or (a[i] <= (b[i]+b[i+1]) <=  (a[i]+a[i+1])):
                k+=1 
       else :
           if (a[i] >= b[i] >= (a[i]+a[i+1]) ) or ( a[i] >= (b[i]+b[i+1]) >= (a[i]+a[i+1])):
                k+=1     
   if k==2 :
       print('si choca')
   else :
       print('no chocan')          
p=input() 
q=input()
p=cordenadas.ints(p)
q=cordenadas.ints(q)
print(p,q)
comparacion(p,q)

#6,3,5,2  4,3,4,2
#9,-3,7,-2  4,3,4,2
