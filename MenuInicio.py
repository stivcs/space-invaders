import pygame
from pygame import mixer
import random
import main
import creditos

pygame.init()  # Inicializar los módulos principales de pygame
pygame.font.init()  # Inicializar el módulo pygame.font
Blanco = (255, 255, 255)  # Definir una tupla que representa el color blanco en formato RGB
transparente = pygame.Color(0,0,0,0)  # Definir un objeto de color de pygame que representa el color negro con transparencia total
fuente = pygame.font.SysFont(None, 50)  # Crear un objeto de fuente de pygame que utiliza la fuente predeterminada del sistema con un tamaño de 50 píxeles

def musica():
    """
    Esta función inicializa el mezclador de sonido de pygame y reproduce en bucle un archivo de sonido llamado 'MusicaLobby.mpeg'.
    """
    pygame.mixer.init()  # Inicializar el mezclador de sonido de pygame
    global sonido  # Definir la variable 'sonido' como global para poder acceder a ella desde fuera de la función
    sonido = pygame.mixer.Sound('Sonidos\MusicaLobby.mpeg')  # Cargar el archivo de sonido en la variable 'sonido'
    sonido.play(loops=-1)  # Reproducir el sonido en bucle
    
def Inicio():
    """
    Esta función crea una ventana de menú para el juego utilizando la biblioteca pygame. Muestra una imagen de fondo y reproduce música de fondo utilizando la función 'musica()'. Si el usuario hace clic en un área específica de la pantalla (entre las coordenadas x de 340 y 457 y las coordenadas y de 381 y 440), se detiene la música del menú, se inicia la música del juego y se llama a la función 'juego()' del módulo 'main'. Si el juego termina, se vuelve al menú principal llamando a esta función nuevamente.
    """
    global sonido  # Definir la variable 'sonido' como global para poder acceder a ella desde dentro de la función
    ventana = pygame.display.set_mode((800,600))  # Crear una ventana de 800x600 píxeles
    pygame.display.set_caption("Space Invaders")  # Establecer el título de la ventana como "Menu"
    ImgMenu = pygame.image.load("Imagenes\FondoInicio.png")  # Cargar una imagen de fondo
    musica()  # Llamar a la función 'musica()' para reproducir música de fondo
    ventana.blit(ImgMenu,(0,0))  # Dibujar la imagen de fondo en la ventana
    pygame.display.update()  # Actualizar la pantalla
    while True:  # Entrar en un bucle infinito para manejar los eventos del usuario
        for eventos in pygame.event.get():  # Iterar sobre todos los eventos recibidos
            if eventos.type == pygame.QUIT:  # Si el evento es cerrar la ventana
                pygame.quit()  # Salir de pygame
                quit()  # Salir del programa
            if eventos.type == pygame.MOUSEBUTTONDOWN:  # Si el evento es hacer clic con el ratón
                if eventos.button == 1:  # Si el botón izquierdo del ratón fue presionado
                    x,y = eventos.pos  # Obtener las coordenadas del clic
                    if x > 340 and x < 457 and y > 381 and y < 440:  # Si el clic fue en un área específica de la pantalla
                        sonido.stop()  # Detener el sonido del menú
                        main.musica()  # Llamar a la función 'musica()' del módulo 'main' para iniciar la música del juego
                        main.juego()   # Llamar a la función 'juego()' del módulo 'main' para iniciar el juego
                        creditos.Final()  # Llamar a la función 'Creditos()' del módulo 'main' para mostrar los créditos
                        #regresar al menu principal
                        Inicio()       # Llamar a esta función nuevamente para volver al menú principal cuando el juego termine
                        
        ventana.blit(ImgMenu,(0,0))      # Dibujar nuevamente la imagen de fondo en cada iteración del bucle
        pygame.display.update()          # Actualizar nuevamente la pantalla en cada iteración del bucle

Inicio()                                 # Llamar a esta función al final para iniciar el menú del juego
