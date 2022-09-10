#CALCULADORA BÁSICA CON MENU
import math

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
bandrea=False
n=int(input("\nIngrese la opcion a realizar: "))
x=float(input("\nIngrese el primer numero 'x': "))
y=float(input("\nIngrese el segundo numero 'Y': "))

#processing
if n==1:
    r=x+y
    print("\nEl resultado de la suma entre "+str(x)+" y "+str(y)+" es: "+str(r)+"\n")
else:
    if n==2:
        r=x-y
        print("\nEl resultado de la resta entre "+str(x)+" y "+str(y)+" es: "+str(r)+"\n")
    else:
        if n==3:
            r=x*y
            print("\nEl resultado de la multiplicacion entre "+str(x)+" y "+str(y)+" es: "+str(r)+"\n")
        else:
            if n==4:
                if y!=0:
                    r=x/y
                    print("\nEl resultado de la division entre "+str(x)+" y "+str(y)+" es: "+str(r)+"\n")
                else:
                    print("\nLa division no se puede realizar, el denominador es igual a cero\n")
            else:
                if n==5:
                    r=x**y
                    print("\nEl resultado de la potencia entre "+str(x)+" y "+str(y)+" es: "+str(r)+"\n")
                else:
                    if n==6:
                        if x>1:
                            r=math.log(y)/math.log(x)
                            print("\nEl resultado del logaritmo base "+str(x)+" y "+str(y)+" es: "+str(r)+"\n")
                        else:
                            print("\nLa base ingresada es menor a cero, no es posible calcular el logaritmo\n")
                    else:
                        print("\nLa opcion ingresada no esta en el menu o es incorrecta\n")