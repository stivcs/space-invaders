import pygame
from pygame import mixer
import random
import math
import tkinter as tk
import guardar

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
FPS = 1000  # Definir la cantidad de cuadros por segundo del juego
RELOJ = pygame.time.Clock()  # Crear un objeto de reloj para controlar los FPS
# Title
pygame.display.set_caption('Space Invaders')


class Player:
    def __init__(self):
        self.playerImg = pygame.image.load('Imagenes\haverecta.png')
        self.naveDer = pygame.image.load('Imagenes\haveder.png')
        self.naveIzq = pygame.image.load('Imagenes\haveizq.png') 
        self.currentImg = self.playerImg
        self.X = 370
        self.Y = 480
        self.playerX_change = 0
    def setXchange(self,xchange):
        self.playerX_change = xchange
    def getX(self):
        return self.X
    def setm(self): 
        self.X += self.playerX_change
        if self.X <= 0:
            self.X = 0
        elif self.X >= 736:
            self.X = 736
    def draw(self):
        screen.blit(self.currentImg, (self.X, self.Y))
class Enemy:
    def __init__(self):
        self.image = pygame.image.load('Imagenes\enemy.png')
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.enemyX_change, self.enemyY_change = 1, 40
    def getY(self):
        return self.y
    def getX(self):
        return self.x
    def setY(self,y):
        self.y = y
    def setX(self,x):
        self.x = x
    def setm(self):
        self.x += self.enemyX_change
        if self.x <= 0:
            self.enemyX_change = 2
            self.y += self.enemyY_change
        elif self.x >=736:
            self.enemyX_change = -2
            self.y += self.enemyY_change
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Enemy2:
    def __init__(self):
        self.image2 = pygame.image.load('Imagenes\enemy2.png')
        self.x2 = random.randint(0, 736)
        self.y2 = random.randint(50, 150)
        self.enemyX_change2, self.enemyY_change2 = 1, 40
    def getY(self):
        return self.y2
    def getX(self):
        return self.x2
    def setY(self,y2):
        self.y2 = y2
    def setX(self,x2):
        self.x2 = x2
    def setm(self):
        self.x2 += self.enemyX_change2
        if self.x2 <= 0:
            self.enemyX_change2 = 1
            self.y2 += self.enemyY_change2
        elif self.x2 >=736:
            self.enemyX_change2 = -1
            self.y2 += self.enemyY_change2
    def draw(self):
        screen.blit(self.image2, (self.x2, self.y2)) 

def musica():
    """
    Carga y reproduce la música de fondo del juego.

    Esta función utiliza la biblioteca Pygame para cargar y reproducir un archivo de música de fondo.
    El archivo de música debe estar ubicado en el directorio "Sonidos" y tener el nombre "MusicaCombate.mpeg".
    La música se reproduce en bucle, es decir, se repetirá continuamente hasta que se detenga explícitamente.
    """
    pygame.mixer.music.load('Sonidos\MusicaCombate.mpeg')  # Carga el archivo de música de fondo
    pygame.mixer.music.play(-1)  # Reproduce la música en bucle (-1 indica que se debe repetir continuamente)

sonido_balazo = pygame.mixer.Sound('Sonidos\laser.wav')  # Cargar un archivo de sonido para reproducir cuando se dispara una bala
# Background
fondo = pygame.image.load("imagenes/fondoPrincipal.png").convert()
y=0
screen.blit(fondo, (0, y))  # Dibujar el fondo en la pantalla

# Bullet
bulletImg = pygame.image.load('Imagenes\Bullet.png')
bulletX, bulletY = 0, 480
bulletX_change, bulletY_change = 0, 3
bullet_state = 'ready'

# Score
score_value = 0

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

def isCollision2(enemyX2, enemyY2, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX2 - bulletX, 2) + math.pow(enemyY2 - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False 

def Creditos():
    Creditos = pygame.image.load('Imagenes\Creditos.png')
    screen.blit(Creditos, (0, 0))
    
#genera posicion aleatorias en la pantalla
coord_list = []
for i in range(40):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    coord_list.append([x,y])
#crea al enemigo y al jugador
enemy = Enemy()
player = Player()
enemy2 = Enemy2()

def juego():
    # Game Loop
    global playerX, playerY, playerX_change, bulletX, bulletY, bulletX_change, bulletY_change, bullet_state, score_value, enemyX, enemyY, enemyX_change, enemyY_change, enemyX2, enemyY2, enemyX_change2, enemyY_change2, y, fondo, currentImg, naveDer, naveIzq, enemyImg, enemyImg2, sonido_balazo, FPS, RELOJ, screen, running
    pygame.init()
    running = True
    while running: 
        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.currentImg = player.naveIzq
                    player.setXchange(-0.5)
                if event.key == pygame.K_RIGHT:
                    player.currentImg = player.naveDer
                    player.setXchange(0.5)
                if event.key == pygame.K_SPACE:
                    if bullet_state == 'ready':
                        bulletX = player.X + (player.playerImg.get_width() // 2) - (bulletImg.get_width() // 2)  # Calcula la posición inicial de la bala  
                        fire_bullet(bulletX, bulletY)
                        sonido_balazo.play()  # Reproduce el sonido de disparo
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.currentImg = player.playerImg
                    player.setXchange(0)
                if event.key == pygame.K_RIGHT:
                    player.setXchange(0)
                if event.key == pygame.K_SPACE:
                    if bullet_state == 'ready':
                        bulletX = player.X + (player.playerImg.get_width() // 2) - (bulletImg.get_width() // 2)  # Calcula la posición inicial de la bala 
                        fire_bullet(bulletX, bulletY)
                        sonido_balazo.play()  # Reproduce el sonido de disparo
        
        player.setm()
        # Movimiento del fondo
        #miro la posición del fondo y la actualizo
        y_relativa = y % fondo.get_rect().height # y_relativa es la posición del fondo en la pantalla
        screen.blit(fondo, (0, y_relativa - fondo.get_rect().height))#dibujo el fondo en la pantalla 
        if y_relativa < 600:
            screen.blit(fondo, (0, y_relativa)) 
        y+=1
        # Control de FPS
        RELOJ.tick(FPS)
        # Actualización de la ventana
        # Enemy
        if enemy.getY() > 440:
            break
        
        if enemy2.getY() > 440:
            break
        #actualiza el movimiento del enemygo
        enemy.setm()
        enemy2.setm()

        collision = isCollision(enemy.getX(), enemy.getY(), bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemy.setX(random.randint(0, 736))
            enemy.setY(random.randint(50, 150))
        #dibuja al enemigo
        enemy.draw()
        
        if score_value % 2 == 0 and score_value != 0:  # Si el valor de puntuación es par y no es cero
                collision2 = isCollision2(enemy2.getX(), enemy2.getY(), bulletX, bulletY)  # Comprueba si hay colisión entre el segundo enemigo y la bala
                if collision2:  # Si hay colisión
                    bulletY = 480  # Reposiciona la bala fuera de la pantalla
                    bullet_state = 'ready'  # Cambia el estado de la bala a 'ready', indicando que está lista para disparar nuevamente
                    score_value += 1  # Incrementa el valor de puntuación en 1
                    enemy2.setX(random.randint(0, 736))  # Reposiciona el segundo enemigo en una ubicación horizontal aleatoria
                    enemy2.setY(random.randint(50, 150))  # Reposiciona el segundo enemigo en una ubicación vertical aleatoria
                enemy2.draw()  # Dibuja el segundo enemigo en la pantalla
        else:
            pass

        
        # Bullet Movement
        if bulletY <=0:
            bulletY = 480
            bullet_state = 'ready'

        if bullet_state == 'fire':
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change  
        
        # Score
        font = pygame.font.SysFont(None, 32) 
        score = font.render("Score : " + str(score_value), True, (255,255,255)) 
        screen.blit(score, (20,50))

        #dibuja al jugador
        player.draw()
        pygame.display.update()

    font = pygame.font.SysFont(None, 50)
    perder = font.render("perdiste game over",True, (255,255,255)) 
    screen.blit(perder, (250,150))
    pygame.display.update()
    pygame.time.delay((1000))
    pygame.quit()


    def centrar_ventana(ventana):
        ventana.update_idletasks()
        width = ventana.winfo_width()
        height = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (width // 2)
        y = (ventana.winfo_screenheight() // 2) - (height // 2)
        ventana.geometry(f"{width}x{height}+{x}+{y}")

    def jugadores():

        nombre = str(ct1.get())
        fecha = str(ct2.get())
        date = guardar.usuario(nombre, fecha, str(score_value))
        guardar.guardardatos(date)
        lec = guardar.leer()
        vg.destroy()
        vj = tk.Tk()
        vj.geometry("400x400")
        vj.config(bg="black")
        vj.title("jugadores")
        centrar_ventana(vj)
        tex = tk.Label(vj,text="APODO\t\tFECHA\t\tSCORE",bg="black",fg="white")
        tex.grid(row=0,column=0)
        tex1 = tk.Label(vj,text=lec,bg="black",fg="white")
        tex1.grid(row=1,column=0)
        vj.mainloop()



    vg = tk.Tk()
    vg.geometry("300x100")
    centrar_ventana(vg)
    vg.title("guardar datos")
    vg.config(bg="black")
    tex1 = tk.Label(vg,text="REGISTRO",bg="black",fg="white")
    tex1.grid(row=1,column=1)
    text2 = tk.Label(vg,text="ingrese apodo",bg="black",fg="white")
    text2.grid(row=2,column=0)
    ct1 = tk.Entry(vg)
    ct1.grid(row=2,column=1)
    text3 = tk.Label(vg,text="ingrese fecha",bg="black",fg="white")
    text3.grid(row=3,column=0)
    ct2 = tk.Entry(vg)
    ct2.grid(row=3,column=1)


    bt1 = tk.Button(vg,text="GUARDAR",command=jugadores , bg="white",fg="black")
    bt1.grid(row=4,column=1)

    vg.mainloop()
