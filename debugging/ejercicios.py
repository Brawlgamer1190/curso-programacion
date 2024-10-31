def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def comparar_con_promedio(numeros, promedio):
    for num in numeros:   
        if num > promedio: #después del if elif y else van ":", en este caso no habian
            print(f"{num} es mayor que el promedio.")
        elif num < promedio:
            print(f"{num} es menor que el promedio.")
        else:
            print(f"{num} es igual al promedio.")

# Pedir al usuario tres números
numeros = []
for i in range(3):
    num = int(input("Introduce un número: ")) #Se necesita pasar los datos ingresados a int para posteriormente usar sum
    numeros.append(num)

# Calcular el promedio
promedio = calcular_promedio(numeros)

# Comparar cada número con el promedio
comparar_con_promedio(numeros, promedio)