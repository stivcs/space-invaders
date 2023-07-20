import pygame
from pygame import mixer
import random

def musica():
    """
    Esta función inicializa el mezclador de sonido de pygame y reproduce en bucle un archivo de sonido llamado 'MusicaCreditos.mpeg'.
    """
    pygame.mixer.init()  # Inicializar el mezclador de sonido de pygame
    global sonido  # Definir la variable 'sonido' como global para poder acceder a ella desde fuera de la función
    sonido = pygame.mixer.Sound('Sonidos\MusicaCreditos.mpeg')  # Cargar el archivo de sonido en la variable 'sonido'
    sonido.play(loops=-1)  # Reproducir el sonido en bucle


def Final():
    """
    Esta función crea una ventana de menú para el juego utilizando la biblioteca pygame. Muestra una imagen de fondo y reproduce música de fondo utilizando la función 'musica()'. Si el usuario hace clic en un área específica de la pantalla (entre las coordenadas x de 340 y 457 y las coordenadas y de 381 y 440), se detiene la música del menú, se inicia la música del juego y se llama a la función 'juego()' del módulo 'main'. Si el juego termina, se vuelve al menú principal llamando a esta función nuevamente.
    """
    global sonido  # Definir la variable 'sonido' como global para poder acceder a ella desde dentro de la función
    ventana = pygame.display.set_mode((800,600))  # Crear una ventana de 800x600 píxeles
    pygame.display.set_caption("Space Invaders")  # Establecer el título de la ventana como "Menu"
    Imgcreditos = pygame.image.load("Imagenes\Creditos.png")  # Cargar una imagen de fondo
    musica()  # Llamar a la función 'musica()' para reproducir música de fondo
    ventana.blit(Imgcreditos,(0,0))  # Dibujar la imagen de fondo en la ventana
    pygame.display.update()  # Actualizar la pantalla
    while True:  # Entrar en un bucle infinito para manejar los eventos del usuario
        for eventos in pygame.event.get():  # Iterar sobre todos los eventos recibidos
            if eventos.type == pygame.QUIT:  # Si el evento es cerrar la ventana
                pygame.quit()  # Salir de pygame
                quit()  # Salir del programa
        
        ventana.blit(Imgcreditos,(0,0))      # Dibujar nuevamente la imagen de fondo en cada iteración del bucle
        pygame.display.update()
