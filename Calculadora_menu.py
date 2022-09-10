#CALCULADORA BÁSICA CON MENU
from math import log

#despliegue de menu
print(" --------------------------------------------------------------------------------")
print("Programa calculadora para dos numeros, escoja la operacion que desea realizar: \n")
print("Ingrese 1 para sumar X+Y")
print("Ingrese 2 para restar X-Y")
print("Ingrese 3 para multiplicar X*Y")
print("Ingrese 4 para dividir X/Y")
print("Ingrese 5 para potencia X^Y")
print("Ingrese 6 para logaritmo Log X ('Y') \n")
print(" ---------------------------------------------------------------------------------")

#input
bandera=False
n=int(input("\nIngrese la opcion a realizar: "))
x=float(input("\nIngrese el primer numero 'x': "))
y=float(input("\nIngrese el segundo numero 'Y': "))

#processing
if n==1:
    r=x+y
    print("\nEl resultado de la suma "+str(x)+"+"+str(y)+" es: ")
elif n==2:
    r=x-y
    print("\nEl resultado de la resta entre "+str(x)+"-"+str(y)+" es: ")
elif n==3:
    r=x*y
    print("\nEl resultado de la multiplicacion "+str(x)+"*"+str(y)+" es: ")
elif n==4 and y!=0:
    r=x/y
    print("\nEl resultado de la division entre "+str(x)+"/"+str(y)+" es: ")
elif n==4 and y==0:
    print("\nLa division no se puede realizar, el denominador es igual a cero\n")
    bandera=True 
elif n==5:
    r=pow(x,y)
    print("\nEl resultado de la potencia entre "+str(x)+"^"+str(y)+" es: ")
elif n==6 and x>1:
    r=log(y)/log(x)
    print("\nEl resultado del logaritmo base "+str(x)+" de "+str(y)+" es: ")
elif n==6 and x<=1:
    print("\nLa base ingresada es menor o igual a uno, no es posible calcular el logaritmo\n")
    bandera=True
else:
    print("\nLa opcion ingresada no esta en el menu o es incorrecta\n")

if n<7 and bandera==False:
    print(r)
    print(" ")
