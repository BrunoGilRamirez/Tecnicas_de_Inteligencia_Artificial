import numpy as np
import matplotlib.pyplot as plt
import random

# Generador de tonos
def generate_shades(n):
    if n <= 1:
        return None
    shades = []
    for i in range(n):
        shade_value = int((i / (n - 1)) * 255)  # Calcula el valor de sombra de 0 a 255
        hex_code = format(shade_value, '02x')  # Convierte el valor de la sombra a formato hexadecimal
        color = '#' + hex_code + hex_code + hex_code  # Crea el código hexadecimal del color repitiendo el valor del tono
        shades.append(color)
    return shades

# Herramienta para ordenar la población en base a la aptitud
def getZ(z):
  return z['Z']

# Función de aptitud
def fitness(x, y):
    return (np.exp(-(y + 1)**2 - x**2)) * ((x - 1)**2) - ((np.exp(-(x + 1)**2))/3) + (np.exp(-x**2 - y**2)) * (10*x**3 - 10*x + 10*y**3)

# Pinta los puntos en la gráfica
def punto3D(x, y, z, ax, color='#000000'):
    ax.scatter(x, y, z, c=color, s=10)

# Crea la grafíca 3D de la función
def grafica3D():
    # Generar datos para la gráfica
    x = np.linspace(-4, 4, 20)
    y = np.linspace(-4, 4, 20)
    X, Y = np.meshgrid(x, y)
    Z = fitness(X, Y)
    
    # Graficar la función
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d', computed_zorder=False)
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)
    ax.view_init(elev=11, azim=0)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    return ax

# Crea la primera generación de puntos
def generate_population(population_size):
    population = []
    for _ in range(population_size):
        x = random.uniform(-4, 4)
        y = random.uniform(-4, 4)
        z = fitness(x, y)
        individual = {'X':x, 'Y':y, 'Z':z}
        population.append(individual)
    return population

# Método de selección por ruleta
def roulette_selection(poblacion, aptitudes):
    min_aptitud = min(aptitudes)
    aptitudes_ajustadas = [aptitud + abs(min_aptitud) for aptitud in aptitudes] #Las aptitudes negativas las hace positivas para poder hacer la suma
    suma_aptitudes = sum(aptitudes_ajustadas)
    aleatorio = random.uniform(0, suma_aptitudes)

    rango_acumulado = 0
    for individuo, aptitud in zip(poblacion, aptitudes_ajustadas):
        rango_acumulado += aptitud
        if rango_acumulado >= aleatorio: #Entre mas alta sea la aptitud, mas probabilidad tiene de ser elegido
            individuo_seleccionado = individuo
            break

    return individuo_seleccionado

# Operación de cruce (cruza promedio)
def crossover_one(parent1, parent2):
    x1, y1 = parent1['X'], parent1['Y']
    x2, y2 = parent2['X'], parent2['Y']
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2

    z = fitness(x, y)
    individual = {'X':x, 'Y':y, 'Z':z}
    return individual

# Operación de cruce (cruza en un punto)
def crossover_two(parent1, parent2):
    x1, y1 = parent1['X'], parent1['Y']
    x2, y2 = parent2['X'], parent2['Y']

    # Generar un punto de corte aleatorio
    cutoff = random.randint(1, 2)

    # Realizar la cruza en el punto de corte
    if cutoff == 1:
        x = x1
        y = y2
    else:
        x = x2
        y = y1

    z = fitness(x, y)
    individual = {'X':x, 'Y':y, 'Z':z}
    return individual

# Operación de mutación (mutación uniforme)
def mutate(individual, mutation_rate):
    # Definir los límites del espacio de búsqueda
    x_min, x_max = -4, 4
    y_min, y_max = -4, 4
    x, y = individual['X'], individual['Y']
    if random.uniform(0,1) < mutation_rate:
        x += random.uniform(-1, 1)
        y += random.uniform(-1, 1)
    # Asegurarse de que el individuo permanezca dentro del espacio de búsqueda
    x = max(min(x, x_max), x_min)
    y = max(min(y, y_max), y_min)
    
    z = fitness(x, y)
    individual = {'X':x, 'Y':y, 'Z':z}
    return individual

def algoritmoGenetico(mutation_rate, n):
    mejor = {}
    tonos = generate_shades(n) #Colores para los puntos
    ax = grafica3D()

    # Genera la primera generación
    poblacion = generate_population(10)
    poblacion.sort(key=getZ) # Ordena la población de menor a mayor aptitud
    for i in poblacion: # Dibuja la primera generación
        punto3D(i['X'], i['Y'], i['Z'], ax)
    mejor = poblacion[9] # Toma la mejor solución de la primera generación

    for j in range(0, n - 1):
        elite1, elite2 = poblacion[9], poblacion[8]
        poblacion = []
        # La siguiente generación incluye los dos mejores de la generación pasada
        poblacion.append(elite1)
        poblacion.append(elite2)
        # Genera la siguiente generación usando la selección por ruleta, dos cruzas y una posible mutación
        for i in range(8):
            padre1 = roulette_selection(poblacion, [i['Z'] for i in poblacion])
            padre2 = roulette_selection(poblacion, [i['Z'] for i in poblacion])
            if i <= 3: # A una mitad hace una cruza y a la otra le aplica otra cruza
                hijo = crossover_one(padre1, padre2)
                hijo = mutate(hijo, mutation_rate)
            else:
                hijo = crossover_two(padre1, padre2)
                hijo = mutate(hijo, mutation_rate)
            poblacion.append(hijo)
            
        poblacion.sort(key=getZ) # Ordena la población de menor a mayor aptitud
        for i in poblacion: # Dibuja la nueva generación
            punto3D(i['X'], i['Y'], i['Z'], ax, tonos[j])

        if mejor['Z'] <= poblacion[9]['Z']: # Busca la mejor solución de todas las generaciones
            mejor = poblacion[9]

    punto3D(mejor['X'], mejor['Y'], mejor['Z'], ax, "#FF0000") # Al mejor lo pinta de rojo
    plt.show()
    return mejor

if __name__ == '__main__':
    mutation_rate = 0.15 # Aumentar la mutación puede dar resultados mas interesantes
    generaciones = int(input("Introduce el número de generaciones: "))
    print(f'La mejor solución: {algoritmoGenetico(mutation_rate, generaciones)}')