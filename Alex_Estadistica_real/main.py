import math

# Leer números del archivo
numeros = []
with open("C:\\Users\\Alex\\Downloads\\las_esferas_del_dragon.txt") as file:
    for line in file:
        numeros.append(float(line.strip()))

# Calcular el rango
minimo = min(numeros)
maximo = max(numeros)
rango = maximo - minimo
n = len(numeros)

# Calcular el número de clases
print("Determine el número de clases:")
print("1. De 5 en 5")
print("2. k=(1+log2(n))")
print("3. Raiz cuadrada de (n)")
print("4. Numero de clases manual")
op = int(input())

if op == 1:
    num_clases = 5
elif op == 2:
    num_clases = math.ceil(1 + math.log(n) / math.log(2))
elif op == 3:
    num_clases = math.ceil(math.sqrt(n))
elif op == 4:
    num_clases = int(input("Ingrese el número de clases manualmente: "))
else:
    print("Opción no válida")
    exit()

intervalo = rango / num_clases
ir = math.ceil(intervalo)

# Calcular los intervalos de clase y las marcas de clase
Li_1 = [minimo + i * ir for i in range(num_clases)]
Li = [Li_1[i] + ir for i in range(num_clases)]
Xi = [(Li_1[i] + Li[i]) / 2 for i in range(num_clases)]

# Frecuencia absoluta (ni)
ni = [0] * num_clases
for num in numeros:
    for i in range(num_clases):
        if Li_1[i] <= num < Li[i]:
            ni[i] += 1
            break

# Frecuencia absoluta acumulada Ni
Ni = [sum(ni[:i+1]) for i in range(num_clases)]

# Calcular los porcentajes de las frecuencias
hi = [(ni[i] / n) * 100 for i in range(num_clases)]

# Frecuencia absoluta acumulada en porcentaje
Hi = [sum(hi[:i+1]) for i in range(num_clases)]

# Imprimir los resultados
print("El numero de clases es: ", num_clases)
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("El rango es:", rango)
print("El tamaño del intervalo es (sin redondear):", intervalo)
print("El tamaño del intervalo es:", ir)
print("\t\t-----------------------------------------------------")
print("|N.clases|\tLi-1-Li\t\tXi\tni\tNi\thi\tHi")
print("\t\t-----------------------------------------------------")
for i in range(num_clases):
    print(f"{i+1}\t\t[{Li_1[i]:.2f}\t{Li[i]:.2f})\t{Xi[i]:.2f}\t{ni[i]}\t{Ni[i]:.2f}\t{hi[i]:.2f}\t{Hi[i]:.2f}")
    print("\t\t-----------------------------------------------------")
