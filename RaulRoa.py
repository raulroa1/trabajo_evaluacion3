import numpy as np
menu=True
multas=0
datos_vehiculo=np.array([])
valor_multa=0
while menu:
    print("------------------------AUTO SEGURO------------------------\n 1.-Grabar \n 2.-Buscar \n 3.-Imprimir certificados \n 4.-Salir")
    Opcion=int(input("Seleccione la opcion a elegir:"))
    if Opcion >=1 or Opcion <=4:
        if Opcion==1:
            print("------------------------AUTO SEGURO------------------------\n Has seleccionado la opcion (1.-GRABAR)")
            tipo_auto=str(input("Escriba el tipo de vehiculo a Grabar en sistema: \nEj:Deportivo\n"))
            patente_auto=input("Introduzca la patente del vehiculo a Grabar: \nEj:VW-YP-47\n")
            marca_auto=str(input("Introduzca la marca del vehiculo: \nEj:Mercedes Benz\n"))
            precio_vehiculo=(input("Introduzca el valor a pagar por el Vehiculo: \nMonto Minimo:$5.000.000\n"))
            fecha_de_registro=input("Introduzca la fecha del registro:\nFORMATO DD/MM/AA\n")
            nombre_dueño=str(input("Introduzca el nombre de el dueño de el vehiculo:\n Formato Nombre y Apellido\n"))
            print("El vehiculo posee multas? \n1.-Si\n2.-No\n")
            multas=int(input("Digite una opcion:"))
            datos_vehiculo=[tipo_auto,patente_auto,marca_auto,precio_vehiculo,fecha_de_registro,nombre_dueño]
            if multas==1:
                print("------------------------AUTO SEGURO------------------------")
                valor_multa=(input("Ingrese el valor de la multa:"))
                fecha_multa=input("Ingrese la fecha de la multa:\nFormato DD/MM/AA\n")
                datos_vehiculo2=datos_vehiculo[valor_multa,fecha_multa]
        elif Opcion==2:
            print("------------------------AUTO SEGURO------------------------\n Has seleccionado la opcion (2.-Buscar)")
            buscar_patente=input("Introduzca la patente del vehiculo a Buscar")
            
            if buscar_patente==datos_vehiculo2[1]:
                print(f"------------------------AUTO SEGURO------------------------\n Los datos encontrados segun la patente {buscar_patente}, se encontro lo siguiente:")
                print("Tipo de vehiculo:", datos_vehiculo[0])
                print("Marca del auto:", datos_vehiculo[2])
                print("Valor del vehiculo:", datos_vehiculo[3])
                print(f"Fecha del ingreso del vehiculo:", datos_vehiculo[4])
                print(f"El dueño de el vehiculo es:", datos_vehiculo[5])
                print("El vehiculo posee una multa de:", datos_vehiculo[-1]) 
                print("La fecha de la multa es el dia", datos_vehiculo[7])
            else:
                print("La patente ingresada no tiene datos")
        elif Opcion==3:
            print("------------------------AUTO SEGURO------------------------\nHas ingresado la opcion (3.-Imprimir certificados)")
            print("\n1.-Imprimir cetificado de Emisión de contaminantes\n 2.-Imprimir cetificado de Anotaciones vigentes 3.-Imprimir cetificado de Multas.")
        elif Opcion==4:
            print("Has salido del menu")
            menu=False
    else:
        print("Opcion seleccionada no valida")   
else:
    print("Has salido del menu")