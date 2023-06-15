#sin argumentos y sin retorno
def saludo ():
    print("saludando a mis estudiantes")
saludo()
saludo()
saludo()
#sin argumentos con retorno
def suma1():
    num_1=10
    num_2=5
    resultado=num_1+num_2
    return resultado
resultado_suma=suma1()
print("Forma A de utilizar funcion con retorno:",resultado_suma)
print("Forma B de utilizar funcion con retorno:",suma1())
#funcion con argumento y sin retorno
def resta1(num_1,num_2):
    resultado=num_1-num_2
    print("El resultado de la resta es:", resultado )
resta1(10,1)

#funcion con argumento y con retorno
def resta2(num_1,num_2):
    resultado=num_1-num_2
    return resultado
resultado_1=resta2(10,1)#9
resultado_2=resta2(8,3)#5
#forma decente
print(resultado_1-resultado_2)#4
#forma bizarra
print(resta2(10,1)+resta2(8,3))#14