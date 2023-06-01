import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

from Perceptron import Perceptron


class EntrenamientoDropdown(DropDown):
    def __init__(self, **kwargs):
        super(EntrenamientoDropdown, self).__init__(**kwargs)


class ReconocimientoDropdown(DropDown):
    pass


class PerceptronWindow(BoxLayout):
    entradas = np.array([])
    pesos = np.random.uniform(-1, 1, size=2)
    umbral = np.random.uniform(-1, 1)
    tasa_de_aprendizaje = 0.01
    ciclos = 100
    ciclo = 0
    perceptron: Perceptron = None
    square_a = None
    square_b = None

    def __init__(self):
        super(PerceptronWindow, self).__init__()
        self.graph = self.ids.graph
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        self.graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        self.e_dropdown = EntrenamientoDropdown()
        entrenamiento_button = self.ids.entrenamiento_dropdown
        entrenamiento_button.bind(on_release=self.e_dropdown.open)
        self.e_dropdown.bind(on_select=lambda instance, x: setattr(entrenamiento_button, 'text', x))

        self.r_dropdown = ReconocimientoDropdown()
        reconocimiento_button = self.ids.reconocimiento_dropdown
        reconocimiento_button.bind(on_release=self.r_dropdown.open)
        self.r_dropdown.bind(on_select=lambda instance, x: setattr(reconocimiento_button, 'text', x))

    def cambiar_parametros(self) -> None:
        try:
            int_1, int_2 = float(self.ids.intervalo_1.text), float(self.ids.intervalo_2.text)
            self.pesos = np.random.uniform(int_1, int_2, size=2)

            self.tasa_de_aprendizaje = float(self.ids.tasa_de_aprendizaje.text)

            print(f'New parameters: {self.pesos}, {self.tasa_de_aprendizaje}, {self.ciclos}')
        except ValueError:
            print('Error en los parámetros')

    def generar_regiones(self) -> None:
        try:
            self.ids.region_errors.text = ''
            self.square_a = a = {
                'x1': float(self.ids.ax1.text),
                'y1': float(self.ids.ay1.text),
                'x2': float(self.ids.ax2.text),
                'y2': float(self.ids.ay2.text),
                'n': int(self.ids.na.text)
            }
            self.square_b = b = {
                'x1': float(self.ids.bx1.text),
                'y1': float(self.ids.by1.text),
                'x2': float(self.ids.bx2.text),
                'y2': float(self.ids.by2.text),
                'n': int(self.ids.nb.text)
            }
            self.graph.clear_widgets()

            fig, ax = plt.subplots()

            square_a = Rectangle((a['x1'], a['y1']), a['x2'] - a['x1'], a['y2'] - a['y1'], linewidth=1, edgecolor='r', facecolor='none')
            square_b = Rectangle((b['x1'], b['y1']), b['x2'] - b['x1'], b['y2'] - b['y1'], linewidth=1, edgecolor='b', facecolor='none')

            ax.add_patch(square_a)
            ax.add_patch(square_b)

            ax.set_xlim(min(a['x1'], b['x1']) - 1, max(a['x2'], b['x2']) + 1)
            ax.set_ylim(min(a['y1'], b['y1']) - 1, max(a['y2'], b['y2']) + 1)

            plt.xlabel('x - axis')
            plt.ylabel('y - axis')

            self.graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))

            points_a = np.random.uniform(low=[a['x1'], a['y1']], high=[a['x2'], a['y2']], size=(a['n'], 2))
            points_a = np.hstack((points_a, np.zeros((a['n'], 1))))

            points_b = np.random.uniform(low=[b['x1'], b['y1']], high=[b['x2'], b['y2']], size=(b['n'], 2))
            points_b = np.hstack((points_b, np.ones((b['n'], 1))))

            self.entradas = np.concatenate((points_a, points_b))

            print(f'Entradas: {self.entradas}')

            nombre_archivo = self.ids.file_name.text
            np.savetxt(f'data/{nombre_archivo}.csv', self.entradas, delimiter=',')

        except ValueError:
            self.ids.region_errors.text = 'Error: Las coordenadas deben ser números'

    def entrenar(self) -> None:
        if self.ids.entrenamiento_dropdown.text == 'Entrenamiento':
            self.ids.entrenamiento_label.text = 'Entrenamiento      (Elige una opción)'
            return None

        if self.ids.entrenamiento_dropdown.text == 'Pintar por paso':
            self.ids.entrenamiento_label.text = 'Entrenamiento'
            self.graph.clear_widgets()

            self.perceptron = Perceptron(
                self.entradas,
                self.pesos,
                self.umbral,
                self.tasa_de_aprendizaje,
                self.ciclos
            )

            self.ciclo = 0
            Clock.schedule_interval(self.pintar_por_paso, 0.1)

        if self.ids.entrenamiento_dropdown.text == 'Pintar por inicio y final':
            self.ids.entrenamiento_label.text = 'Entrenamiento'

            self.perceptron = Perceptron(
                self.entradas,
                self.pesos,
                self.umbral,
                self.tasa_de_aprendizaje,
                self.ciclos
            )

            self.perceptron.entrenar()
            self.graph.clear_widgets()

            if hasattr(self, "scatter"):
                self.scatter.remove()
            self.scatter = plt.scatter(self.entradas[:, 0], self.entradas[:, 1], c=self.entradas[:, 2])
            x_min, x_max = plt.xlim()
            y_min, y_max = plt.ylim()
            xx, yy = np.meshgrid(np.linspace(x_min, x_max), np.linspace(y_min, y_max))
            grid = np.c_[xx.ravel(), yy.ravel()]
            Z = np.array([self.perceptron.activacion(entrada=x) for x in grid])
            Z = Z.reshape(xx.shape)
            if hasattr(self, "decision_boundary"):
                self.decision_boundary.remove()
            self.decision_boundary = plt.contour(xx, yy, Z, colors='k', levels=[0])
            plt.xlabel('x - axis')
            plt.ylabel('y - axis')
            self.graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def detener(self) -> None:
        Clock.unschedule(self.pintar_por_paso)
        self.ciclo = 0

    def reconocer(self) -> None:
        if self.ids.reconocimiento_dropdown.text == 'Reconocimiento':
            self.ids.reconocimiento_label.text = 'Reconocimiento      (Elige una opción)'
            return None

        if self.ids.reconocimiento_dropdown.text == 'Generar datos al azar':

            quantity = self.ids.reconocimiento_quantity.text

            if quantity == '':
                self.ids.reconocimiento_label.text = 'Error: Ingrese un número'
                return None

            try:
                quantity = int(quantity)
            except ValueError:
                self.ids.reconocimiento_label.text = 'Error: Ingrese número valido'
                return None

            self.ids.reconocimiento_label.text = 'Reconocimiento'

            a = self.square_a
            b = self.square_b

            a_size = quantity // 2
            b_size = quantity - a_size

            points_a = np.random.uniform(low=[a['x1'], a['y1']], high=[a['x2'], a['y2']], size=(a_size, 2))
            points_a = np.hstack((points_a, np.zeros((a_size, 1))))

            points_b = np.random.uniform(low=[b['x1'], b['y1']], high=[b['x2'], b['y2']], size=(b_size, 2))
            points_b = np.hstack((points_b, np.ones((b_size, 1))))

            entradas = np.concatenate((points_a, points_b))

        if self.ids.reconocimiento_dropdown.text == 'Cargar un archivo':
            self.ids.reconocimiento_label.text = 'Reconocimiento'
            file_name = self.ids.reconocimiento_archivo.text
            try:
                entradas = np.loadtxt(f'data/{file_name}.csv', delimiter=',')
            except FileNotFoundError:
                self.ids.file_error.text = 'Error: Archivo no encontrado'
                return None

            self.ids.file_error.text = ''

        correct = 0
        total_points = len(entradas)
        nuevas_entradas = np.copy(entradas)

        print(f'SQUARE: {self.square_a}')

        for indice, entrada in enumerate(entradas):
            predicted_class = self.perceptron.activacion(entrada=entrada[:-1])
            nuevas_entradas[indice][-1] = predicted_class

            x, y = entrada[0], entrada[1]

            if (self.square_a['x1'] <= x <= self.square_a['x2']) and (self.square_a['y1'] <= y <= self.square_a['y2']):
                print(f"Point {entrada} is inside square_a")
                correct += 1

            if (self.square_b['x1'] <= x <= self.square_b['x2']) and (
                    self.square_b['y1'] <= y <= self.square_b['y2']):
                print(f"Point {entrada} is inside square_b")
                correct += 1

        print(f'Correct: {correct}')
        print(f'Total: {total_points}')
        print(f'Accuracy: {correct / total_points}')
        print(f'Percentage: {correct / total_points * 100}%')
        self.ids.percentages_label.text = f'Porcentaje {correct / total_points * 100} %'

        self.graph.clear_widgets()

        if hasattr(self, "scatter"):
            self.scatter.remove()
        self.scatter = plt.scatter(nuevas_entradas[:, 0], nuevas_entradas[:, 1], c=nuevas_entradas[:, 2])
        x_min, x_max = plt.xlim()
        y_min, y_max = plt.ylim()
        xx, yy = np.meshgrid(np.linspace(x_min, x_max), np.linspace(y_min, y_max))
        grid = np.c_[xx.ravel(), yy.ravel()]
        Z = np.array([self.perceptron.activacion(entrada=x) for x in grid])
        Z = Z.reshape(xx.shape)
        if hasattr(self, "decision_boundary"):
            self.decision_boundary.remove()
        self.decision_boundary = plt.contour(xx, yy, Z, colors='k', levels=[0])
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        self.graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def pintar_por_paso(self, *args) -> None:
        print(f'Ciclo: {self.ciclo}')
        if self.ciclo >= self.ciclos:
            Clock.unschedule(self.pintar_por_paso)
            self.ciclo = 0
            return None

        self.perceptron.entrenar_por_paso()
        self.ciclo += 1

        if hasattr(self, "scatter"):
            self.scatter.remove()
        self.scatter = plt.scatter(self.entradas[:, 0], self.entradas[:, 1], c=self.entradas[:, 2])
        x_min, x_max = plt.xlim()
        y_min, y_max = plt.ylim()
        xx, yy = np.meshgrid(np.linspace(x_min, x_max), np.linspace(y_min, y_max))
        grid = np.c_[xx.ravel(), yy.ravel()]
        Z = np.array([self.perceptron.activacion(entrada=x) for x in grid])
        Z = Z.reshape(xx.shape)
        if hasattr(self, "decision_boundary"):
            self.decision_boundary.remove()
        self.decision_boundary = plt.contour(xx, yy, Z, colors='k', levels=[0])
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')

        self.graph.clear_widgets()
        self.graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class PerceptronApp(App):
    def build(self) -> PerceptronWindow:
        return PerceptronWindow()
