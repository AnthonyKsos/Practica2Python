################
## PROBLEMA 1 ##
################

# Contador para números que cumplen las condiciones
contador = 0

# Iterar sobre el rango de 1500 a 2700
for i in range(1500, 2701):
    # Verificar condiciones
    if  i % 7 == 0 and i % 5 == 0:
        print(i)
        contador += 1

print(f"Cantidad de numeros divisibles por 7 y multiplos de 5: {contador}")


################
## PROBLEMA 2 ##
################

# Pedir al usuario
num = int(input("Ingrese el numero de asteriscos para generar el patron: "))

# Generar la mitad superior
for i in range(1,num+1):
    print("* "* i)

# Mitad inferior
for i in range(num-1,0,-1):
    print("* "* i)


################
## PROBLEMA 3 ##
################

lista = []
while True:
    # Pedir al usuario si desea continuar
    rpt = input("¿Desea ingresar un número?: ")
    if rpt == 'Si' or rpt == 'SI' or rpt == 'si':
        # Anadir a la lista el numero
        num = int(input("Ingrese el número: "))
        lista.append(num)
    else:
        # Contar pares e impares
        npares = 0
        nimpares = 0
        for i in lista:
            if i % 2 == 0:
                npares += 1
            else:
                nimpares += 1

        # Imprimir
        print("\nNúmeros ingresados:", lista)
        print(f"Cantidad de numeros pares: {npares}")
        print(f"Cantidad de numeros impares: {nimpares}")
        break


################
## PROBLEMA 4 ##
################

lista_alumnos = [] # Lista general de todos los alumnos
num_alumnos = int(input("Ingrese el número de alumnos en el colegio: "))

# Pedir información por cada alumno
for i in range(num_alumnos):
    lista_nota = [] # Lista de notas
    nombre = input("Ingrese el nombre del alumno: ")

    # Añadir 3 notas por alumno a una lista
    for a in range(3):
        lista_nota.append(int(input(f"Ingrese la nota {a+1} de {nombre}: ")))
    
    info = {
        "nombre": nombre,
        "notas" : lista_nota
    }
    lista_alumnos.append(info)

# Imprimir nombre y notas por alumno
print("\nListado completo de los alumnos")
for i in range (len(lista_alumnos)):
    print(f"\nAlumno {i+1}")
    print(f"Nombre: {lista_alumnos[i]['nombre']}")
    print("Notas:", lista_alumnos[i]['notas'])


################
## PROBLEMA 5 ##
################

def contar_digitos (numero, digito):
    return numero.count(digito) # Contar cuántos digitos hay en el número

numero = input("Ingrese un numero entero: ")
digito = input("Ingrese un digito: ")

contar = contar_digitos(numero, digito) # Llama función

print(f"Numero ingresado: {numero} y Dígito: {digito}")
print(f"Cantidad de veces {digito} en el número: {contar}")


################
## PROBLEMA 6 ##
################

def serie_fibonacci (fin):
    lista = [0, 1]
    indice = 1
    fibonacci = 1

    # Mientras el número hallado a través de la serie de fibonacci sea menor al numero ingresado por usuario
    while fibonacci <= int(fin):
        fibonacci = lista[indice] + lista[indice - 1] # Hallar fibonacci
        lista.append(fibonacci)
        indice += 1
    
    # Remueve el último fibonacci porque el while primero evalúa la condición antes de hallar el fibonacci
    lista.remove(fibonacci)
    return lista

fin = input("Ingrese el fin de la serie de fibonacci: ")
print(f"Serie de fibonacci hasta {fin}:", *serie_fibonacci(fin))


################
## PROBLEMA 7 ##
################

def esPrimo (num):
    divisores = 0 # Contador

    for i in range(1, num+1):
        if num % i == 0: # Evaluando si es divisor del numero
            divisores += 1
    
    return divisores == 2 # Si tiene 2 divisores, es número primo

numero = int(input("Ingrese un numero: "))
print(f"El numero es primo?:", esPrimo(numero))


################
## PROBLEMA 8 ##
################

# Factorial (forma recursiva)
def factorial (numero):
    if numero == 0:
        return 1
    else:
        return numero*factorial(numero-1)

n = int(input("Ingrese un numero: "))

# Validación
if (n < 0):
    print("Debe ingresar un numero entero no negativo")
else:
    resultado = factorial(n)
    print(f"El factorial del número {n} es: {resultado}")


################
## PROBLEMA 9 ##
################

def quitar_vocales (cadena):
    vocales = "aeiouAEIOU"
    nueva_cadena = ""
    for i in cadena:
        # Si no contiene un elemento de la lista vocales, lo añade 
        if i not in vocales:
            nueva_cadena += i

    return nueva_cadena

cadena = input("Input: ")
resultado = quitar_vocales(cadena)
print(f"Output: {resultado}")


#################
## PROBLEMA 10 ##
#################

def cambiar_formato_fecha(cadena):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    # Caso 1: Formato "MM DD, AAAA"
    if ',' in cadena:
        mes, resto = cadena.split(' ', 1) # 2 cadenas: 'MM' y 'DD, AAAA'
        dia, anio = resto.split(', ') # 2 cadenas: 'DD' y 'AAAA'
        mes_numero = meses.index(mes) + 1  # Convertir nombre de mes a número
        return f"{anio}-{mes_numero:02d}-{int(dia):02d}"

    # Caso 2: Formato "MM/DD/AAAA"
    else:
        m, d, a = cadena.split('/')
        return f"{a}-{int(m):02d}-{int(d):02d}"

# Solicitar fecha al usuario
fecha = input("Ingrese una fecha (MM DD, AAAA o MM/DD/AAAA): ")
fecha_formateada = cambiar_formato_fecha(fecha)
print(f"Fecha formateada: {fecha_formateada}")