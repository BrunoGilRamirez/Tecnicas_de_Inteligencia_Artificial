import numpy as np
import matplotlib.pyplot as plt

"""
    Datos de 14 personas -> [edad, ahorro]
    Estos con el fin de entrenar al Perceptron
"""
personas = np.array([[0.1, 0.7], [0.2, 0.6],
                     [0.3, 0.4], [0.4, 0.3],
                     [0.3, 0.2], [0.4, 0.1], 
                     [0.5, 0.2], [0.4, 0.8],
                     [0.6, 0.8], [0.5, 0.6], 
                     [0.7, 0.6], [0.8, 0.5],
                     [0.9, 0.4], [0.9, 0.2]])

# 1 : aprobrada    0 : denegada
clases = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]) # Salidas esperadas para supervisar el entrenamiento

"""
    El peso y el umbral(b) es asignado de manera aleatoria
    La taza de aprendizaje es que tanto se modificaran el umbral y los pesos al momento de encontrar un error
    Las epocas es la cantidad de veces que el perceptron sera entrenado para que llegue a tener los mejores resultados
"""
pesos = np.random.uniform(-1, 1, size=2)
b = np.random.uniform(-1, 1)
tasa_de_aprendizaje = 0.01
epocas = 200

# Gráfica de dispersión (edad, ahorro)
# plt.figure(figsize=(7, 7))
# plt.title("¿Tarjeta Platinum?", fontsize=20)
# plt.scatter(personas[clases == 0].T[0], 
#             personas[clases == 0].T[1], 
#             marker="x", s=180, color="red",
#             linewidths=5, label="Denegada")
# plt.scatter(personas[clases == 1].T[0],
#             personas[clases == 1].T[1], 
#             marker="o", s=180, color="blue",
#             linewidths=5, label="Aprobada")
# plt.xlabel("Edad", fontsize=15)
# plt.ylabel("Ahorro", fontsize=15)
# plt.legend(bbox_to_anchor=(1.3, 0.15))
# plt.box(False)
# plt.xlim((0, 1.01))
# plt.ylim((0, 1.01))
# plt.grid()
# plt.show()

"""
    pesos: Asignados aleatoriamente
    x: Valores de entrada
    b: Umbral
"""
def activacion(pesos, x, b):
    z = pesos * x
    if z.sum() + b > 0:
        return 1
    else:
        return 0

#Entrenamiento del perceptron
for epoca in range(epocas):
    error_total = 0
    for i in range(len(personas)):
        prediccion = activacion(pesos, personas[i], b)
        error = clases[i] - prediccion
        error_total += error**2
        pesos[0] += tasa_de_aprendizaje * personas[i][0] * error
        pesos[1] += tasa_de_aprendizaje * personas[i][1] * error
        b += tasa_de_aprendizaje * error 
    print(error_total, end=" ")

print(f'\n{activacion(pesos, [0.5, 0.5], b)}')

# Gráfica de dispersión (edad, ahorro)
plt.figure(figsize=(6, 5), dpi=200)
plt.title("¿Tarjeta Platinum?", fontsize=20)

plt.scatter(personas[clases == 0].T[0], 
            personas[clases == 0].T[1], 
            marker="x", s=180, color="red",
            linewidths=5, label="Denegada")

plt.scatter(personas[clases == 1].T[0],
            personas[clases == 1].T[1], 
            marker="o", s=180, color="blue",
            linewidths=5, label="Aprobada")

for edad in np.arange(0, 1, 0.05):
    for ahorro in np.arange(0, 1, 0.05):
        color = activacion(pesos, [edad, ahorro], b)
        if color == 1:
            plt.scatter(edad, ahorro, marker="s", s=110,
                        color="blue", alpha=0.2, linewidths=0)
        else:
            plt.scatter(edad, ahorro, marker="s", s=110, 
                        color="red", alpha=0.2, linewidths=0)
            
plt.xlabel("Edad", fontsize=15)
plt.ylabel("Ahorro", fontsize=15)
plt.legend(bbox_to_anchor=(1.3, 0.15))
plt.box(False)
plt.xlim((0, 1.01))
plt.ylim((0, 1.01))
plt.show()