from abc import ABC
from jugador import Jugador

class Menu(ABC):
    def __init__(self):
        pass

class MenuInicio(Menu):
    def __init__(self):
        self.menu_juego = MenuJuego()

    def inicio(self):
        while True:
            print(f'Bienvenido a DCCivilizations! \n\n'
                  f'Seleccione una opción:          \n'
                  f'[1] Crear partida               \n'
                  f'[2] Cargar partida              \n')

            decision = input(f'Indique su opción (1 o 2): ')
            
            if decision == '1':
                self.menu_crear_partida()
                self.menu_juego.menu_turno_jugador()

            elif decision == '2':
                self.menu_cargar_partida()
                self.menu_juego.menu_turno_jugador()
            
            else:
                print('Esta opción es inválida')
    
    def menu_crear_partida(self):
        while True:
            print('¿A qué civilización quieres pertenecer? \n'
                  '[1] DCC                                 \n'
                  '[2] La Comarca                          \n'
                  '[3] Cobreloa                            \n'
                  '[4] Volver atrás                        \n')
            
            decision = input(f'Selecciona tu opción (1, 2, 3 o 4): ')

            if decision == '1':
                pass
            
            elif decision == '2':
                pass
            
            elif decision == '3':
                pass
            
            elif decision == '4':
                break

            else:
                print('Esta opción es inválida')

    
    def menu_cargar_partida(self):
        pass

class MenuJuego(Menu):
    def __init__(self):
        self.jugador = Jugador()

    def menu_turno_jugador(self):

        while True:
            print(f'Es tu turno! ¿Que quieres hacer? \n'
                  f'[1] Recolectar recursos          \n'
                  f'[2] Crear personas               \n'
                  f'[3] Crear edificios              \n'
                  f'[4] Atacar civilización          \n'
                  f'[5] Esperar turno                \n'
                  f'[6] Investigar otras civilizaciones \n'
                  f'[7] Guardar partida \n'
                  f'[8] Guardar partida y salir \n'
                  f'[9] Salir sin guardar \n'
                  f'[10] Volver atrás \n')
            
            decision = input()

            if decision == '1':
                self.jugador.recolectar_recursos()
            
            elif decision == '2':
                self.jugador.crear_personas()
            
            elif decision == '3':
                self.jugador.crear_edficios()
            
            elif decision == '4':
                self.jugador.atacar_civilizacion()
            
            elif decision == '5':
                self.jugador.esperar_turno()
            
            elif decision == '6':
                self.jugador.investigar_otras_civilizaciones()
            
            elif decision == '7':
                pass
            
            elif decision == '8':
                pass
            
            elif decision == '9':
                pass
            
            elif decision == '10':
                break 

            else:
                print('Esta decisión es inválida')


