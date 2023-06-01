from logger_base import log

"""
Perceptron:
Un perceptrón es una neurona artificial, y, por tanto, una unidad de red neuronal. El perceptrón efectúa cálculos para detectar características o tendencias en los datos de entrada. Se trata de un algoritmo para el aprendizaje supervisado de clasificadores binarios.
"""


class Perceptron:
    '''
    Este es un perceptron que trabaja con varios valores para ser entrenado y perfeccionado, así posteriormente clasificar los nuevos valores de entrada en base a los criterios que el perceptron mismo establecio gracias al entrenamiento supervisado que realizo.
    '''
    def __init__(self, entradas, pesos, umbral, aprendizaje, ciclos):
        '''
        entradas: Son los datos de entrada.
        salidas: Son las salidas o bien resultado de las entradas que seran usadas como entrenamiento.
        pesos: Son números asociados a las entradas que se multiplicaran con estas.
        umbral: Determina la sensibilidad de la función de activación.
        aprendizaje: Determina la calibración del umbral y de los pesos.
        ciclos: Determina la cantidad de veces que el perceptron requiera entrenar para perfeccionar su clasificación.
        '''
        self._entradas = entradas[:, :-1]
        self._salidas = entradas[:, -1]
        self._pesos = pesos
        self._umbral = umbral
        self._aprendizaje = aprendizaje
        self._ciclos = ciclos
    
    def activacion(self, entrada):
        '''
        Con pesos y umbral establecidos, recibe la entrada a clasificar y retorna el resultado binario.
        '''
        sigma = self._pesos * entrada
        if sigma.sum() + self._umbral > 0:
            return 1
        else:
            return 0
        
    def entrenar(self):
        '''
        Entrena al perceptron en base a las entradas y sus salidas esperadas, y en base a los errores, calibra en cada ciclo el umbral y los pesos para perfeccionar el calculo en la función de activación.
        '''
        for ciclo in range(self._ciclos):
            errores_totales = 0 #Contador de errores para checar si se calibra correctamente el perceptron
            for i in range(len(self._entradas)):
                prediccion = self.activacion(entrada=self._entradas[i])
                error = self._salidas[i] - prediccion
                errores_totales += error**2 #Contador de errores
                self._umbral += self._aprendizaje * error #Calibración del umbral
                for j in range(len(self._entradas[i])): #Calibración de los pesos
                    self._pesos[j] += self._aprendizaje * self._entradas[i][j] * error
            # log.debug(errores_totales)

    def entrenar_por_paso(self):
        errores_totales = 0
        for i in range(len(self._entradas)):
            prediccion = self.activacion(entrada=self._entradas[i])
            error = self._salidas[i] - prediccion
            errores_totales += error ** 2
            self._umbral += self._aprendizaje * error
            for j in range(len(self._entradas[i])):
                self._pesos[j] += self._aprendizaje * self._entradas[i][j] * error
        # log.debug(errores_totales)
