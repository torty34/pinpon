def verificacion():
    while  0==0 : 
        valor = input("Ingrese un número entero: ")
        try:
            valor = int(valor)
            break            
        except ValueError:
            print( "ATENCIÓN: Debe ingresar un número entero.")
    print('cargando...')     
    return valor
def hola():
    print('hola') 
       