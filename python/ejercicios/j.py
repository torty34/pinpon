v= [4,2,7,5,3]
for i in range(len(v)-1):
    for j in range(i,len(v)-1):
        if v[j+1]<v[i]:
           a=v[j+1]
           v[j+1]=v[i]
           v[i]=a  
print(v)            