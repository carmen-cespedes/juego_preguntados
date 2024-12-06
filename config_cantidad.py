import pygame
from colores import *
from fuentes import *
from constantes import *
from funciones import *
from pantalla_puntos import *





def pantalla_configuracion_tiempo(pantalla, fuente, tiempo_actual):
    
    configurando = True
    nuevo_tiempo = str(tiempo_actual)  # Mostrar el tiempo actual como texto
    
    while configurando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Presionar ENTER para confirmar
                    configurando = False
                elif evento.key == pygame.K_BACKSPACE:  # Borrar el último carácter
                    nuevo_tiempo = nuevo_tiempo[:-1]
                else:
                    nuevo_tiempo += evento.unicode  # Añadir carácter

        # Dibujar la pantalla de configuración
        pantalla.fill(FONDO)
        texto_titulo = fuente.render("Configurar tiempo por pregunta:", True, WHITE)
        texto_tiempo = fuente.render(nuevo_tiempo, True, PURPLE)
        texto_instrucciones = fuente.render("Presiona ENTER para guardar.", True, WHITE)
        
        pantalla.blit(texto_titulo, (150, 200))
        pantalla.blit(texto_tiempo, (350, 300))
        pantalla.blit(texto_instrucciones, (150, 400))
        pygame.display.flip()

#------puntos------


def pantalla_menu_configuracion_puntos(cantidad_de_puntos_facil, cantidad_de_puntos_intermedio, cantidad_de_puntos_dificil):
    pygame.init()
    
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Preguntados - Cantidad de Puntos") # nombre del juego
    icono = pygame.image.load("icono.png") # path de la imagen
    icono = pygame.transform.scale(icono, (350, 200)) # redimensiono la imagen
    pygame.display.set_icon(icono) # icono del juego
    
    texto = fuente_titulo.render("MODIFICAR PUNTOS", True, PURPLE)
    texto_boton_cantidad_de_puntos_facil = fuente_boton.render("puntos facil", True, WHITE)
    texto_boton_cantidad_de_puntos_intermedio = fuente_boton.render("puntos intermedio", True, WHITE)
    texto_boton_cantidad_de_puntos_dificil = fuente_boton.render("puntos dificil", True, WHITE)
    texto_boton_salir = fuente_boton.render("Volver", True, WHITE)
    
    
    # botones
    boton_cantidad_de_puntos_facil = pygame.Rect(190, 280, 410, 50)
    boton_cantidad_de_puntos_intermedio = pygame.Rect(190, 360, 410, 50)
    boton_cantidad_de_puntos_dificil = pygame.Rect(190, 440, 410, 50)
    boton_salir = pygame.Rect(190, 530, 410, 50)
    
    
    bandera = True
    
    while bandera:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_posicion = pygame.mouse.get_pos()
                if boton_cantidad_de_puntos_facil.collidepoint(mouse_posicion):
                    puntos_facil = config_puntos_facil(pantalla, fuente_boton, cantidad_de_puntos_facil)
                    print(f"Puntos facil: {cantidad_de_puntos_facil}")
                if boton_cantidad_de_puntos_intermedio.collidepoint(mouse_posicion):
                    puntos_intermedio = config_puntos_intermedio(pantalla, fuente_puntos, cantidad_de_puntos_intermedio)
                if boton_cantidad_de_puntos_dificil.collidepoint(mouse_posicion):
                    puntos_dificil = config_puntos_dificil(pantalla, fuente_puntos, cantidad_de_puntos_dificil)
                if boton_salir.collidepoint(mouse_posicion):
                    bandera = False
    
        # rellenar pantalla con un color
        pantalla.fill(ORANGE)
        
        
        # dibujar el boton
        pygame.draw.rect(pantalla, (PURPLE), boton_cantidad_de_puntos_facil)
        pygame.draw.rect(pantalla, (PURPLE), boton_cantidad_de_puntos_intermedio)
        pygame.draw.rect(pantalla, (PURPLE), boton_cantidad_de_puntos_dificil)
        pygame.draw.rect(pantalla, (PURPLE), boton_salir)
        
        pantalla.blit(icono, DIMENSION_ICONO)
        
        # dimension para texto titulo
        dimension_texto_x = calcular_centro_pantalla((ANCHO,ALTO), texto.get_size())
        dimension_texto_y = 17
        pantalla.blit(texto, (dimension_texto_x, dimension_texto_y))
        
        # dimension para texto boton cantidad de puntos
        dimension_texto_boton_puntos_facil_x = calcular_centro_pantalla((ANCHO, ALTO),texto_boton_cantidad_de_puntos_facil.get_size())
        dimension_texto_boton_puntos_facil_y = 280
        pantalla.blit(texto_boton_cantidad_de_puntos_facil, (dimension_texto_boton_puntos_facil_x, dimension_texto_boton_puntos_facil_y))
        
        # dimension para texto boton cantidad de puntos
        dimension_texto_boton_puntos_intermedio_x = calcular_centro_pantalla((ANCHO, ALTO),texto_boton_cantidad_de_puntos_intermedio.get_size())
        dimension_texto_boton_puntos_intermedio_y = 360
        pantalla.blit(texto_boton_cantidad_de_puntos_intermedio, (dimension_texto_boton_puntos_intermedio_x, dimension_texto_boton_puntos_intermedio_y))
        
        # dimension para texto boton cantidad de puntos
        dimension_texto_boton_puntos_dificil_x = calcular_centro_pantalla((ANCHO, ALTO),texto_boton_cantidad_de_puntos_dificil.get_size())
        dimension_texto_boton_puntos_dificil_y = 440
        pantalla.blit(texto_boton_cantidad_de_puntos_dificil, (dimension_texto_boton_puntos_dificil_x, dimension_texto_boton_puntos_dificil_y))
        
        # dimension para texto boton salir
        dimension_salir_x = calcular_centro_pantalla((ANCHO, ALTO), texto_boton_salir.get_size())
        dimension_salir_y = 530
        pantalla.blit(texto_boton_salir, (dimension_salir_x, dimension_salir_y))
        
        
        pygame.display.flip()
        
    return puntos_facil, puntos_intermedio, puntos_dificil

#-------vidas----

def pantalla_configuracion_vidas(pantalla, fuente, vidas_actual):
    configurando = True
    nuevo_vidas = str(vidas_actual)  # Mostrar el tiempo actual como texto
    
    while configurando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Presionar ENTER para confirmar
                    if nuevo_vidas == "":
                        nuevo_vidas = 1
                    configurando = False
                elif evento.key == pygame.K_BACKSPACE:  # Borrar el último carácter
                    nuevo_vidas = nuevo_vidas[:-1]
                elif evento.unicode.isdigit():
                    nuevo_vidas += evento.unicode
                    
        # Dibujar la pantalla de configuración
        pantalla.fill(PURPLE)
        texto_titulo = fuente.render("Configurar cantidad de vidas:", True, WHITE)
        texto_puntos = fuente.render(nuevo_vidas, True, ORANGE)
        texto_instrucciones = fuente.render("Presiona ENTER para guardar.", True, WHITE)
        
        pantalla.blit(texto_titulo, (150, 200))
        pantalla.blit(texto_puntos, (350, 300))
        pantalla.blit(texto_instrucciones, (150, 400))
        pygame.display.flip()
    
    nuevo_vidas_int = int(nuevo_vidas)
    return nuevo_vidas_int
