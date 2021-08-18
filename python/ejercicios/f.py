def caracol(c):
    nn=[ [0 for columna in range(c)] for columna in range(c)]
    h=(c*4)-4
    h2=(3*4)-4
    h3=h+h2
    for j in range(c):
        for i in range(c):
            ii=i+1
            hji=h-(j+i-1)
            if j==0:
                nn[j][i]=ii
            if j==1 and i!=(c-1):
                nn[j][i]=h+i
            if j==1 and i==(c-1):
                nn[j][i]=j+ii
            if  j==(c//2) and i==0:
                nn[j][i]=h-1
            if  j==(c//2) and i==1:
                nn[j][i]=h3
            if  j==(c//2) and i==2:
                nn[j][i]=c*c
            if  j==(c//2) and i==3:
                nn[j][i]=h3-i
            if  j==(c//2) and i==4:
                nn[j][i]=ii+j
            if j==3 and i==0:
                nn[j][i]=hji
            if j==3 and i>0 and i<c:   
                nn[j][i]=h3-i
            if j==3 and i==4:
                nn[j][i]=ii+j
            if j==4 and i<c:
                nn[j][i]=hji       
    return nn
d=caracol(5)
for k in range(5):
    print (d[k])