menu=True

def menu1():
    print("----------------BIENVENIDO A LA CALCULADORA DE ROA---------------\n1.-Suma\n2.-Resta\n3.-Multiplicar\n4.-Dividir\n5.-Salir")
def suma1():
    resultado=num_1+num_2
    return resultado
def resta1():
    resultado=num_1-num_2
    return resultado
def multiplicacion1():
    resultado=num_1*num_2
    return resultado
def division1():
    resultado=num_1/num_2
    return resultado
def menu2():
    print("----------------LA CALCULADORA DE ROA---------------")
    
while menu:
    menu1()
    opcion1=int(input("Ingrese una opcion"))
    if opcion1==1:
        menu2()
        print("Has seleccionado la opcion 1.-Suma")
        num_1=int(input("INGRESE UN NUMERO PARA SUMAR:"))
        num_2=int(input("INGRESE EL SEGUNDO NUMERO A SUMAR:"))
        print("El resultado de la suma es:",suma1())
    elif opcion1==2:
        menu2()
        print("Has seleccionado la opcion 2.-Resta")
        num_1=int(input("INGRESE UN NUMERO PARA RESTAR:"))
        num_2=int(input("INGRESE EL SEGUNDO NUMERO A RESTAR:"))
        print("El resultado de la resta es:",resta1())
    elif opcion1==3:
        menu2()
        print("Has seleccionado la opcion 3.-Multiplicacion")
        num_1=int(input("INGRESE UN NUMERO PARA MULTIPLICAR:"))
        num_2=int(input("INGRESE EL SEGUNDO NUMERO A MULTIPLICAR:"))
        print("El resultado de la multiplicacion es:",multiplicacion1())
    elif opcion1==4:
        menu2()
        print("Has seleccionado la opcion 4.-Dividir")
        num_1=int(input("INGRESE UN NUMERO PARA DIVIDIR:"))
        num_2=int(input("INGRESE EL SEGUNDO NUMERO A DIVIDIR:"))
        print("El resultado de la division es:",division1())
    else:
        print("Has salido del menu")
        menu=False
