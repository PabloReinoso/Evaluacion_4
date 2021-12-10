import pygame, sys
from pygame.locals import *
import random

#Tamaño de pantalla
ANCHO = 1000
ALTO = 600
#Control de FPS
FPS = 30
#Paleta de colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AMARILLO = (255,233,0)

#Fuentes
consolas = pygame.font.match_font('consolas')


#Creamos la clase jugador
class Jugador(pygame.sprite.Sprite):
    #Sprite del jugador
    def __init__(self):
        #Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Rectangulo (jugador)
        self.image = pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/jugador.png").convert()
        self.image.set_colorkey(BLANCO)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 30
        #Centra el rectangulo (sprite)
        self.rect.center = (500, 600)
        #Velocidad del personaje (inicial)
        self.velocidad_x = 0
        self.velocidad_y = 0
        #Vida del jugadora
        self.hp = 100
        self.bandera = True

    def update(self):
        # Velocidad predeterminada cada vuelta del bucle si no pulsas nada
        self.velocidad_x = 0
        self.velocidad_y = 0

        #Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()

        #Mueve al personaje hacia la izquierda
        if teclas[pygame.K_a]:
            self.velocidad_x = -15
        #Mueve al personaje hacia la derecha
        if teclas[pygame.K_d]:
            self.velocidad_x = 15
        #Mueve al personaje hacia la arriba
        if teclas[pygame.K_w]:
            self.velocidad_y = -15
        #Mueve al personaje hacia la abajo
        if teclas[pygame.K_s]:
            self.velocidad_y = 15
        #Hace que el personaje dispare
        if teclas[pygame.K_SPACE]:
            jugador.disparo()
        if teclas[pygame.K_ESCAPE]:
            self.bandera = False

        #ACtualiza la velocidad del personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #Limita el margen izquierdo
        if self.rect.left < 0:
            self.rect.left = 0
        #Limita el margen derecho
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        #Limita el margen superior
        if self.rect.top < 0:
            self.rect.top = 0
        #Limita el margen inferior
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

    def disparo(self):
        bala = Disparos(self.rect.centerx, self.rect.top + 30)
        balas.add(bala)

#Creamos la clase enemigo
class EnemigoNegro(pygame.sprite.Sprite):
    #Sprite del enemigo
    def __init__(self):
        #Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Rectangulo (enemigo)
        self.image = pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/enemigo.png").convert()
        self.image.set_colorkey(BLANCO)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 50
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        # Velocidad del enemigo (inicial)
        self.velocidad_x = random.randrange(1,3)
        self.velocidad_y = random.randrange(1,3)

    def update(self):
        #Actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x += 1
        # Limita el margen derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # Limita el margen superior
        if self.rect.top < 0:
            self.velocidad_y += 1
        # Limita el margen inferior
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
class EnemigoAmarillo(pygame.sprite.Sprite):
    #Sprite del enemigo
    def __init__(self):
        #Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Rectangulo (enemigo)
        self.image = pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/enemigo1.png").convert()
        self.image.set_colorkey(BLANCO)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 50
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        # Velocidad del enemigo (inicial)
        self.velocidad_x = random.randrange(3,5)
        self.velocidad_y = random.randrange(3,5)

    def update(self):
        #Actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x += 1
        # Limita el margen derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # Limita el margen superior
        if self.rect.top < 0:
            self.velocidad_y += 1
        # Limita el margen inferior
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
class EnemigoAzul(pygame.sprite.Sprite):
    #Sprite del enemigo
    def __init__(self):
        #Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Rectangulo (enemigo)
        self.image = pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/enemigo2.png").convert()
        self.image.set_colorkey(BLANCO)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 50
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        # Velocidad del enemigo (inicial)
        self.velocidad_x = random.randrange(5,10)
        self.velocidad_y = random.randrange(5,10)

    def update(self):
        #Actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x += 1
        # Limita el margen derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # Limita el margen superior
        if self.rect.top < 0:
            self.velocidad_y += 1
        # Limita el margen inferior
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
class EnemigoRojo(pygame.sprite.Sprite):
    #Sprite del enemigo
    def __init__(self):
        #Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Rectangulo (enemigo)
        self.image = pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/enemigo3.png").convert()
        self.image.set_colorkey(BLANCO)
        #Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 50
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        # Velocidad del enemigo (inicial)
        self.velocidad_x = random.randrange(10,13)
        self.velocidad_y = random.randrange(10,13)

    def update(self):
        #Actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x += 1
        # Limita el margen derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # Limita el margen superior
        if self.rect.top < 0:
            self.velocidad_y += 1
        # Limita el margen inferior
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1

#Creamos la clase disparo
class Disparos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Heredamos el init de la clase Sprite de pygame
        super().__init__()
        # Rectangulo (disparo)
        self.image = pygame.transform.scale(pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/disparo.png").convert(),(5,35))
        self.image.set_colorkey(BLANCO)
        # Obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        # Velocidad del disparo (inicial)
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y -= 30
        if self.rect.bottom < 0:
            self.kill()

class Entrada():
    def __init__(self):
        self.lineas = 0
        self.caracteres = ['',]
        self.fuente = pygame.font.Font(None,35)
        self.distancia = 20
        self.posX = 485
        self.posY = 310
    def teclas(self,evento):
        for accion in evento:
            if accion.type == KEYDOWN:
                if accion.key == K_RETURN:
                    self.caracteres.append('')
                    self.lineas += 1
                elif accion.key == K_BACKSPACE:
                    if self.caracteres[self.lineas] == '' and self.lineas > 0:
                        self.caracteres = self.caracteres[0:-1]
                        self.lineas -= 1
                    else:
                        self.caracteres[self.lineas] = self.caracteres[self.lineas][0:-1]
                else:
                    self.caracteres[self.lineas] = str(self.caracteres[self.lineas] + accion.unicode)

    def mensaje(self,superficie):
        superficie.fill((0,0,0))
        pygame.draw.rect(PANTALLA, AMARILLO, (375,300,300,50), 3)
        for self.lineas in range(len(self.caracteres)):
            Img_letra = self.fuente.render(self.caracteres[self.lineas],True,(200,200,0))
            superficie.blit(Img_letra,(self.posX,self.posY + self.distancia * self.lineas))

    def mostrar_texto(self):
        print(self.caracteres)

#Iniciacializacion de pygame, creacionde la ventana, titulo y control de reloj
pygame.init()
PANTALLA = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('STAR WARS: STARFIGHTER')
icono = pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/icono.png")
pygame.display.set_icon(icono)
clock = pygame.time.Clock()
escritura = Entrada()

#Sistema de puntuaciones
puntuacion = 0

def muestra_texto(PANTALLA, fuente, texto, color, dimensiones, x, y):
    tipo_letra = pygame.font.Font(fuente,dimensiones)
    superficie = tipo_letra.render(texto,True,color)
    #rectangulo = superficie.get_rect()
    #rectangulo.center(x, y)
    PANTALLA.blit(superficie,(x,y))

def barra_hp(PANTALLA, x, y, hp):
    largo = 200
    ancho = 25
    calculo_barra = int((jugador.hp / 100) * largo)
    borde = pygame.Rect(x, y, largo, ancho)
    rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
    pygame.draw.rect(PANTALLA, NEGRO, borde, 3)
    pygame.draw.rect(PANTALLA, ROJO, rectangulo)
    if jugador.hp < 0:
        jugador.hp = 0

#Grupo de sprites e instanciaciones
sprites = pygame.sprite.Group()
enemigo_negro = pygame.sprite.Group()
enemigo_amarillo = pygame.sprite.Group()
enemigo_azul = pygame.sprite.Group()
enemigo_rojo = pygame.sprite.Group()
balas = pygame.sprite.Group()

#Instancia del jugador principal
jugador = Jugador()
sprites.add(jugador)

#Instancia de enemigos
enemigonegro = EnemigoNegro()
enemigo_negro.add(enemigonegro)
enemigoamarillo = EnemigoAmarillo()
enemigo_amarillo.add(enemigoamarillo)
enemigoazul = EnemigoAzul()
enemigo_azul.add(enemigoazul)
enemigorojo = EnemigoRojo()
enemigo_rojo.add(enemigorojo)

#Musica del juego
pygame.mixer.music.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/sonido.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.0)

#Bucle del juego
ejecutando = True
while ejecutando:
    #Es el que especifica la velocidad del bucle de juego
    clock.tick(FPS)
    eventos = pygame.event.get()
    #Eventos
    for event in eventos:
        #Se cierra y termina el bucle
        if event.type == QUIT:
            ejecutando = False
    pygame.display.update()

    #Actualizacion de sprites
    sprites.update()
    if jugador.bandera == False:
        enemigo_negro.update()
        enemigo_amarillo.update()
        enemigo_azul.update()
        enemigo_rojo.update()
        balas.update()

    #Colisiones jugador contra enemigo
    if jugador.bandera == False:
        colision_nave1 = pygame.sprite.spritecollide(jugador, enemigo_negro,False,pygame.sprite.collide_circle)
        if colision_nave1:
            enemigonegro.kill()
            jugador.hp -= 10
        colision_nave2 = pygame.sprite.spritecollide(jugador, enemigo_amarillo, False, pygame.sprite.collide_circle)
        if colision_nave2:
            enemigoamarillo.kill()
            jugador.hp -= 10
        colision_nave3 = pygame.sprite.spritecollide(jugador, enemigo_azul, False, pygame.sprite.collide_circle)
        if colision_nave3:
            enemigoazul.kill()
            jugador.hp -= 10
        colision_nave4 = pygame.sprite.spritecollide(jugador, enemigo_rojo, False, pygame.sprite.collide_circle)
        if colision_nave4:
            enemigorojo.kill()
            jugador.hp -= 10
        if jugador.hp <= 0:
            jugador.kill()
            enemigonegro.kill()
            enemigoamarillo.kill()
            enemigoazul.kill()
            enemigorojo.kill()
            ejecutando = False

    #Colisiones bala contra enemigos
    colision_negro = pygame.sprite.groupcollide(enemigo_negro,balas,False,True,pygame.sprite.collide_circle)
    if colision_negro:
        enemigonegro.image = pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/explosion.png").convert()
        enemigonegro.image.set_colorkey(NEGRO)
        enemigonegro.velocidad_y += 30
    elif enemigonegro.rect.top > ALTO:
        enemigonegro.kill()
    if colision_negro:
        puntuacion += 10
    colision_amarillo = pygame.sprite.groupcollide(enemigo_amarillo, balas, False, True, pygame.sprite.collide_circle)
    if colision_amarillo:
        enemigoamarillo.image = pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/explosion.png").convert()
        enemigoamarillo.image.set_colorkey(NEGRO)
        enemigoamarillo.velocidad_y += 30
    elif enemigoamarillo.rect.top > ALTO:
        enemigoamarillo.kill()
    if colision_amarillo:
        puntuacion += 25
    colision_azul = pygame.sprite.groupcollide(enemigo_azul, balas, False, True, pygame.sprite.collide_circle)
    if colision_azul:
        enemigoazul.image = pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/explosion.png").convert()
        enemigoazul.image.set_colorkey(NEGRO)
        enemigoazul.velocidad_y += 30
    elif enemigoazul.rect.top > ALTO:
        enemigoazul.kill()
    if colision_azul:
        puntuacion += 50
    colision_rojo = pygame.sprite.groupcollide(enemigo_rojo, balas, False, True, pygame.sprite.collide_circle)
    if colision_rojo:
        enemigorojo.image = pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/explosion.png").convert()
        enemigorojo.image.set_colorkey(NEGRO)
        enemigorojo.velocidad_y += 30
    if enemigorojo.rect.top > ALTO:
        enemigorojo.kill()
    if colision_rojo:
        puntuacion += 100
    if not enemigo_negro and not enemigo_amarillo and not enemigo_azul and not enemigo_rojo and ejecutando == True:
        enemigoamarillo = EnemigoAmarillo()
        enemigo_amarillo.add(enemigoamarillo)
        enemigonegro = EnemigoNegro()
        enemigo_negro.add(enemigonegro)
        enemigoazul = EnemigoAzul()
        enemigo_azul.add(enemigoazul)
        enemigorojo = EnemigoRojo()
        enemigo_rojo.add(enemigorojo)

    #Fondo de pantalla y dibujo de sprites
    fondo = pygame.image.load("C:/Users/julit/OneDrive/Imágenes/JUEGO/fondo.png")
    PANTALLA.blit(fondo,(0,0))
    sprites.draw(PANTALLA)
    enemigo_negro.draw(PANTALLA)
    enemigo_amarillo.draw(PANTALLA)
    enemigo_azul.draw(PANTALLA)
    enemigo_rojo.draw(PANTALLA)
    balas.draw(PANTALLA)
    if jugador.bandera == True:
        escritura.teclas(eventos)
        escritura.mensaje(PANTALLA)
    #Actualiza el contenido de la pantalla
    pygame.display.flip()

    #Dibuja los textos en la pantalla
    muestra_texto(PANTALLA, consolas, str(puntuacion).zfill(7), ROJO, 40,40,15)
    barra_hp(PANTALLA, 750, 15, jugador.hp)
    if jugador.bandera == True:
        muestra_texto(PANTALLA, consolas, str('Ingrese nombre:'), AMARILLO,30,400,250)
escritura.mostrar_texto()

pygame.quit()
def nombre_jugador():
    print(escritura.mostrar_texto())


import socket
import threading
username = str(escritura.mostrar_texto())
print(username)
host = '0.0.0.0'
port = 4444
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "@username":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error Ocurred")
            client.close
            break
def write_messages():
    while True:
        message = f"{username}: {input('')}"
        client.send(message.encode('utf-8'))
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()
write_thread = threading.Thread(target=write_messages)
write_thread.start()

print()
print('Puntaje obtenido: '+str(puntuacion))
