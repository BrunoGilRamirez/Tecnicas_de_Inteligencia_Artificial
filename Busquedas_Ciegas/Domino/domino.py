import random
import time
from maquina import jugador_Maquina as maquina

class Domino:
    def __init__(self): #constructor de la clase Domino
        self.fichas = [(i, j) for i in range(7) for j in range(i, 7)] #genera las fichas del juego
    
    def generar_fichas(self): #genera las fichas del juego
        return self.fichas.copy() #retorna las fichas del juego
    
    def repartir_fichas(self): #reparte las fichas a los jugadores
        fichas_jugador_1 = []
        fichas_jugador_2 = []
        
        fichas_disponibles = self.generar_fichas() #se generan las fichas del juego
        random.shuffle(fichas_disponibles) #se mezclan las fichas del juego
        
        while len(fichas_disponibles) > 0:
            fichas_jugador_1.append(fichas_disponibles.pop()) #se reparten las fichas al jugador 1
            fichas_jugador_2.append(fichas_disponibles.pop()) #se reparten las fichas al jugador 2
        
        return fichas_jugador_1, fichas_jugador_2
        
class Juego_Domino:
    def __init__(self, fichas_jugador_1, fichas_jugador_2): #constructor de la clase Juego_Domino
        self.tablero = []
        self.fichas_jugador_1 = fichas_jugador_1 #fichas del jugador 1
        self.fichas_jugador_2 = fichas_jugador_2 #fichas del jugador 2
        self.ficha_central = (6, 6) #ficha central del juego
        self.turno = 0 #turno del juego

    def decidir_turno(self):
        if  self.ficha_central in self.fichas_jugador_1: #si la ficha central esta en las fichas del jugador 1
            return 1 #retorna 1
        elif self.ficha_central in self.fichas_jugador_2: #si la ficha central esta en las fichas del jugador 2
            return 2 #retorna 2
        
    def determinar_ganador(self,mesa, fichas_jugador_1, fichas_jugador_2, skip): #determina el ganador del juego
        if len(fichas_jugador_1) == 0:  #si el jugador 1 no tiene fichas, gana el jugador 1
            return 1
        elif len(fichas_jugador_2) == 0: #si el jugador 2 no tiene fichas, gana el jugador 2
            return 2
        elif skip>=2: #si los dos jugadores no pueden jugar, gana el jugador con menos fichas
            suma_fichas_jugador_1 = sum(sum(ficha) for ficha in fichas_jugador_1) #suma las fichas del jugador 1
            suma_fichas_jugador_2 = sum(sum(ficha) for ficha in fichas_jugador_2) #suma las fichas del jugador 2
            if suma_fichas_jugador_1 < suma_fichas_jugador_2: #si la suma de las fichas del jugador 1 es menor a la suma de las fichas del jugador 2, gana el jugador 1
                print(f"Gana el jugador 1 con {suma_fichas_jugador_1} puntos y el jugador 2 perdio con {suma_fichas_jugador_2} puntos")
                return 1
            else:
                print(f"Gana el jugador 2 con {suma_fichas_jugador_2} puntos y el jugador 1 perdio con {suma_fichas_jugador_1} puntos")
                 #si la suma de las fichas del jugador 2 es menor a la suma de las fichas del jugador 1, gana el jugador 2
                return 2 #si la suma de las fichas del jugador 2 es menor a la suma de las fichas del jugador 1, gana el jugador 2
        else:
            return None
        
    def string_to_tuple(self, string): #convierte un string a una tupla
        val=-1
        try:
            string.replace("(", "")
            string.replace(")", "") 
            val=tuple(map(int, string.split(",")))
        except:
            pass
        return val
    
    def jugar(self): #funcion que inicia el juego
        maquina1 = maquina(self.fichas_jugador_2, self.tablero) #se crea la maquina
        turno = self.decidir_turno() #se decide el turno
        if turno == 1: #si el turno es 1, empieza el jugador 1
            print("Empieza el jugador 1, las fichas se digitan como x,y")
            time.sleep(4)
            self.tablero.append(self.ficha_central), self.fichas_jugador_1.remove(self.ficha_central) #se agrega la ficha central al tablero y se elimina de las fichas del jugador 1
            turno = 2 #turno de la maquina
        elif turno == 2: #si el turno es 2, empieza el jugador 2
            print("Empieza la computadora")
            time.sleep(2)
            self.tablero.append(self.ficha_central), self.fichas_jugador_2.remove(self.ficha_central) #se agrega la ficha central al tablero y se elimina de las fichas del jugador 2
            turno = 1 #turno del jugador 1
        self.skip=0 #contador de turnos sin jugar
        while (ganador := self.determinar_ganador(self.tablero, self.fichas_jugador_1, self.fichas_jugador_2,self.skip)) is None: #mientras no haya un ganador
            print("--------------------------------------Tablero--------------------------------------------")
            print(f"\n\nFichas en la mesa: {self.tablero}\n\n")
            print("--------------------------------------Tablero--------------------------------------------\n")
            time.sleep(2)
            if turno == 1: #turno del jugador 1
                print("Turno del jugador 1")
                print(f"Fichas del jugador 1: {self.fichas_jugador_1}")
                ficha = input("Si desea Saltar turno solo presione enter, de lo contrario...\nIngrese la ficha que desea jugar: ")
                ficha = self.string_to_tuple(ficha)
                if ficha==-1:
                    self.skip+=1
                if ficha in self.fichas_jugador_1: #si la ficha esta en las fichas del jugador 1
                    if ficha[0]==self.tablero[0][0] :
                        self.tablero.insert(0, ficha[::-1]) #se invierte la ficha y se agrega al tablero
                        self.fichas_jugador_1.remove(ficha)
                        self.skip=0
                    elif ficha[1]==self.tablero[0][0]: #si el primer numero de la ficha es igual al primer numero de la ficha del tablero
                        self.tablero.insert(0, ficha)
                        self.fichas_jugador_1.remove(ficha)
                        self.skip=0
                    elif ficha[1]==self.tablero[-1][1]: #si el segundo numero de la ficha es igual al segundo numero de la ficha del tablero
                        self.tablero.append(ficha[::-1]) #se invierte la ficha y se agrega al tablero
                        self.fichas_jugador_1.remove(ficha)
                        self.skip=0
                    elif ficha[0]==self.tablero[-1][1]: #si el primer numero de la ficha es igual al segundo numero de la ficha del tablero
                        self.tablero.append(ficha)
                        self.fichas_jugador_1.remove(ficha)
                        self.skip=0
                    else:
                        print("El jugador decidio no jugar")
                else:
                    print("No tiene esa ficha")
                turno = 2
            elif turno == 2:
                print("\nTurno de la computadora")
                print(f"Fichas de la maquina: {self.fichas_jugador_2}")
                ficha = maquina1.jugar(self.fichas_jugador_2, self.tablero) #se obtiene la ficha que jugara la maquina
                print(f"La computadora jugo la ficha {ficha}\n")
                time.sleep(2)
                if ficha==-1: #si la ficha es -1, la maquina no puede jugar
                    self.skip+=1 #se aumenta el contador de turnos sin jugar
                if ficha in self.fichas_jugador_2:
                    if ficha[0]==self.tablero[0][0] : 
                        self.tablero.insert(0, ficha[::-1])
                        self.fichas_jugador_2.remove(ficha)
                        self.skip=0
                    elif ficha[1]==self.tablero[0][0]: 
                        self.tablero.insert(0, ficha)
                        self.fichas_jugador_2.remove(ficha)
                        self.skip=0
                    elif ficha[1]==self.tablero[-1][1]:
                        self.tablero.append(ficha[::-1])
                        self.fichas_jugador_2.remove(ficha)
                        self.skip=0
                    elif ficha[0]==self.tablero[-1][1]:
                        self.tablero.append(ficha)
                        self.fichas_jugador_2.remove(ficha)
                        self.skip=0
                    else:
                        print("La computadora decide pasar")
                else:
                    print("No tiene esa ficha")
                turno = 1
            
        print(f"El ganador es el jugador {ganador}")

        
domino = Domino() #se crea el objeto domino
jugador1, jugador2 = domino.repartir_fichas() #se reparten las fichas
juego = Juego_Domino(jugador1, jugador2) #se crea el objeto juego
juego.jugar() #se inicia el juego








