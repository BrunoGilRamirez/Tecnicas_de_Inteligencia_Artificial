import random

class Domino:
    def __init__(self):
        self.fichas = [(i, j) for i in range(7) for j in range(i, 7)]
    
    def generar_fichas(self):
        return self.fichas.copy()
    
    def repartir_fichas(self):
        fichas_jugador_1 = []
        fichas_jugador_2 = []
        
        fichas_disponibles = self.generar_fichas()
        random.shuffle(fichas_disponibles)
        
        while len(fichas_disponibles) > 0:
            fichas_jugador_1.append(fichas_disponibles.pop())
            fichas_jugador_2.append(fichas_disponibles.pop())
        
        return fichas_jugador_1, fichas_jugador_2
        
class Juego_Domino:
    def __init__(self, fichas_jugador_1, fichas_jugador_2):
        self.tablero = []
        self.fichas_jugador_1 = fichas_jugador_1
        self.fichas_jugador_2 = fichas_jugador_2
        self.ficha_central = (6, 6)
        self.turno = 0
    def decidir_turno(self):
        if  self.ficha_central in self.fichas_jugador_1:
            return 1
        elif self.ficha_central in self.fichas_jugador_2:
            return 2
    def determinar_ganador(self,mesa, fichas_jugador_1, fichas_jugador_2, skip):
        if len(fichas_jugador_1) == 0:
            return 1
        elif len(fichas_jugador_2) == 0:
            return 2
        elif skip>=2:
            suma_mesa = sum(sum(ficha) for ficha in mesa)
            suma_fichas_jugador_1 = sum(sum(ficha) for ficha in fichas_jugador_1)
            suma_fichas_jugador_2 = sum(sum(ficha) for ficha in fichas_jugador_2)
            
            if suma_fichas_jugador_1 < suma_fichas_jugador_2:
                return 1
            else:
                return 2
        else:
            return None
    def string_to_tuple(self, string):
        val=-1
        try:
            string.replace("(", "")
            string.replace(")", "")
            val=tuple(map(int, string.split(",")))
        except:
            pass
        return val
    def jugar(self):
        turno = self.decidir_turno()
        if turno == 1:
            print("Empieza el jugador 1")
            self.tablero.append(self.ficha_central), self.fichas_jugador_1.remove(self.ficha_central)
            turno = 2
        elif turno == 2:
            print("Empieza el jugador 2")
            self.tablero.append(self.ficha_central), self.fichas_jugador_2.remove(self.ficha_central)
            turno = 1
        self.skip=0
        while (ganador := self.determinar_ganador(self.tablero, self.fichas_jugador_1, self.fichas_jugador_2,self.skip)) is None:
            if turno == 1:
                print("Turno del jugador 1")
                print(f"Fichas del jugador 1: {self.fichas_jugador_1}")
                print(f"Fichas en la mesa: {self.tablero}")
                ficha = input("Ingrese la ficha que desea jugar: ")
                ficha = self.string_to_tuple(ficha)
                if ficha==-1:
                    self.skip+=1
                if ficha in self.fichas_jugador_1:
                    if ficha[0]==self.tablero[0][0] :
                        self.tablero.insert(0, ficha[::-1])
                        self.fichas_jugador_1.remove(ficha)
                        self.skip=0
                    elif ficha[1]==self.tablero[0][0]: 
                        self.tablero.insert(0, ficha)
                        self.fichas_jugador_1.remove(ficha)
                        self.skip=0
                    elif ficha[1]==self.tablero[-1][1]:
                        self.tablero.append(ficha[::-1])
                        self.fichas_jugador_1.remove(ficha)
                        self.skip=0
                    elif ficha[0]==self.tablero[-1][1]:
                        self.tablero.append(ficha)
                        self.fichas_jugador_1.remove(ficha)
                        self.skip=0
                    else:
                        print("No se puede jugar esa ficha")
                else:
                    print("No tiene esa ficha")
                turno = 2
            elif turno == 2:
                print("Turno del jugador 2")
                print(f"Fichas del jugador 2: {self.fichas_jugador_2}")
                print(f"Fichas en la mesa: {self.tablero}")
                ficha = input("Ingrese la ficha que desea jugar: ")
                ficha = self.string_to_tuple(ficha)
                if ficha==-1:
                    self.skip+=1
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
                        print("No se puede jugar esa ficha")
                else:
                    print("No tiene esa ficha")
                turno = 1
            print(ganador)
            print(self.tablero)
            print(self.fichas_jugador_1)
            print(self.fichas_jugador_2)
            print(f" jugador {turno}")
        print(f"El ganador es el jugador {ganador}")

        
domino = Domino()
jugador1, jugador2 = domino.repartir_fichas()
#print(f"jugador 1: {jugador1} \njugador 2: {jugador2}")
juego = Juego_Domino(jugador1, jugador2)
juego.jugar()








