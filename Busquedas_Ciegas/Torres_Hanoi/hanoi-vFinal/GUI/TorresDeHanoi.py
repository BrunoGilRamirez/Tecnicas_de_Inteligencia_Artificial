from kivy.app import App # Se importa la clase App de kivy
from kivy.uix.label import Label # Se importa la clase Label de kivy
from kivy.uix.boxlayout import BoxLayout # Se importa la clase BoxLayout de kivy
from kivy.uix.recycleview import RecycleView # Se importa la clase RecycleView de kivy
from kivy.uix.button import Button # Se importa la clase Button de kivy
from kivy.clock import Clock # Se importa la clase Clock de kivy


class Disk(Label): # Clase que representa un disco en la interfaz gráfica

    def __init__(self, **kwargs): # Constructor de la clase
        super().__init__(**kwargs) # Se llama al constructor de la clase padre


class TowerRecycleView(RecycleView): # Clase que representa una torre en la interfaz gráfica

    def __init__(self, **kwargs): # Constructor de la clase
        super(TowerRecycleView, self).__init__(**kwargs) # Se llama al constructor de la clase padre
        self.data = [] # Se inicializa la lista de datos
        self.scroll_y = 0 # Se inicializa el scroll en y en 0


class HanoiWindow(BoxLayout): # Clase que representa la ventana principal de la interfaz gráfica
    moves = 0 # Número de movimientos
    pos_hint = {'center_x': .5, 'center_y': .5} # Posición de los discos, se centran en la torre en x y en y.
    path_found = [] # Lista de estados que se deben mostrar en la interfaz gráfica

    def __init__(self, hanoi_algorithm, time_interval=5, **kwargs): # Constructor de la clase principal
        super(HanoiWindow, self).__init__(**kwargs) # Se llama al constructor de la clase padre (BoxLayout)
        self.ids.time_slider.value = time_interval # Se inicializa el valor del slider de tiempo en el valor especificado
        self.algorithm = hanoi_algorithm # Se inicializa el algoritmo de las torres de hanoi a utilizar.
        self.disk_hint_widths = 1
        self.disk_widths = {}

    def start(self): # Método que se encarga de iniciar el algoritmo de las torres de hanoi
        self.moves = 0 # Se inicializa el número de movimientos en 0
        self.ids.tower3.data = [] # Se inicializan los datos de la torre 3

        numero_discos = self.ids.disk_slider.value
        est_inicial = [[i for i in range(numero_discos, 0, -1)], [], []]
        est_final = [[], [], [i for i in range(numero_discos, 0, -1)]]

        found, path = self.algorithm(est_inicial, est_final)
        self.path_found = path

        if not found:
            raise Exception('No se encontró camino')

        time_interval = float(self.ids.time_label.text)

        self.disk_widths = {path[0][0][i]: self.disk_hint_widths * .75 ** i for i in range(len(path[0][0]))}
        print(self.disk_widths)
        self.ids.tower1.data = [{'text': str(key), 'size_hint_x': value, 'pos_hint': self.pos_hint} for key, value in self.disk_widths.items()][::-1]

        event = Clock.schedule_interval(self.start_path_found, time_interval)
        event()

    def start_path_found(self, *args): # Método que se encarga de mostrar el camino encontrado en la interfaz gráfica
        if len(self.path_found) > 0:
            self.ids.tower1.disks = self.path_found[0][0] # Se actualizan los discos de la torre 1
            self.ids.tower1.data = [{ # Se actualizan los datos de la torre 1
                'text': str(i), # Se agrega el texto del disco
                'size_hint_x': self.disk_widths[i], # Se agrega el tamaño del disco
                'pos_hint': self.pos_hint # Se agrega la posición del disco
            } for i in self.ids.tower1.disks][::-1] # Se invierte la lista para que se vean en orden
            self.ids.tower2.disks = self.path_found[0][1] # Se actualizan los discos de la torre 2
            self.ids.tower2.data = [{ # Se actualizan los datos de la torre 2
                'text': str(i), # Se agrega el texto del disco
                'size_hint_x': self.disk_widths[i], # Se agrega el tamaño del disco
                'pos_hint': self.pos_hint # Se agrega la posición del disco
            } for i in self.ids.tower2.disks][::-1] # Se invierte la lista para que se vean en orden
            self.ids.tower3.disks = self.path_found[0][2] # Se actualizan los discos de la torre 3
            self.ids.tower3.data = [{ # Se actualizan los datos de la torre 3
                'text': str(i), # Se agrega el texto del disco
                'size_hint_x': self.disk_widths[i], # Se agrega el tamaño del disco
                'pos_hint': self.pos_hint # Se agrega la posición del disco
            } for i in self.ids.tower3.disks][::-1] # Se invierte la lista para que se vean en orden
            self.path_found.pop(0) # Se elimina el primer elemento de la lista de estados
            self.ids.moves.text = f'Movimientos: {self.moves}' # Se actualiza el número de movimientos
            self.moves += 1 # Se incrementa el número de movimientos
        else: # Si ya no hay más estados que mostrar
            return False  # Se detiene el evento

    def add_disk_test(self): # Método que agrega un disco a la torre 1
        self.ids.tower1.disks.append(len(self.ids.tower1.disks) + 1) # Se agrega un disco a la torre 1, se le suma 1 para que no se repitan los discos
        self.ids.tower1.data = [{'text': str(i)} for i in self.ids.tower1.disks][::-1] # Se agregan los discos a la torre 1, se invierte la lista para que se vean en orden.


class HanoiApp(App):
    algorithm = None

    # noinspection PyMethodMayBeStatic
    def build(self) -> HanoiWindow: # Método que construye la interfaz gráfica
        if self.algorithm is None: # Si no se ha especificado el algoritmo, se lanza una excepción
            raise Exception('No se ha especificado el algoritmo') # Se lanza una excepción indicando que no se ha especificado el algoritmo
        return HanoiWindow(self.algorithm) # Se retorna la ventana principal de la interfaz gráfica
