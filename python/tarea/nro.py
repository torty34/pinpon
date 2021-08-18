import cordenadas
import random
def nroa():
    file = open('torti.txt','w')
    for k in range (100):
        file.write((str(random.randint(1,100)))+' '+(str(random.randint(1,100))+'\n'))
    file.close()
def imprimir():
    file = open('torti.txt')

    mat = [ [0 for columna in range(2)] for columna in range(100)]
    i=0
    for linea in file:
        a=(linea)+','
        a=cordenadas.ints(a)
        for j in range(2):
            mat[i][j]=a[j]
        #print(mat[i][0],mat[i][1])
        i+=1    
    return mat
#n_ale()   
#~h=imprimir()
