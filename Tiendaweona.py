menu=True
import numpy as np

precio_producto=[]
def calcular_iva():
    valor_total=precio_producto[1]*1.19
    return valor_total
while menu:
    print("--------------BIENVENIDO A LA TIENDA ELZA PATITO-------------\n1.-Calcular el iva de mi producto\n2.-Calcular el descuento 3.-Calcular mi Indice de mada corporal")
    opcion=int(input("Seleccione una opcion:"))
    if opcion==1:
        print("--------------TIENDA ELZA PATITO-------------\nHas seleccionado la opcion Calcular el iva de mi producto")
        valor_total=int(input("INGRESE EL VALOR TOTAL DE SU PRODUCTO"))
        np.append=[valor_total]
        print("El monto del iva de su producto es de:", calcular_iva())
        