import pygame
from colores import *
from funciones import *
from constantes import *
import csv
from pantalla_estadist import *

# Inicializar pygame
pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Estadisticas")


# Configuración de la tabla
x = 80
y = 150
espaciado = 50

# Fuente para mostrar texto
fuente = pygame.font.Font(None, 36)


def leer_archivo(nombre_archivo: str, columna_clave: str, columna_valor: str):
    """
    Lee un archivo CSV y retorna los valores de una columna específica según una clave.
    """
    lista_datos = []

    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            if columna_clave in fila and columna_valor in fila:
                clave = fila[columna_clave]
                valor = fila[columna_valor]
                lista_datos.append([clave, valor])  # Almacena la clave y el valor
    return lista_datos





def mostrar_porcentaje_aciertos(pantalla, estadisticas, fuente, ANCHO, ALTO):
    """
    Dibuja el porcentaje de aciertos en la pantalla.
    """
    pantalla.fill(ORANGE)
    titulo = fuente.render("Estadísticas - Porcentaje de Aciertos", True, WHITE)
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))

    # Configuración de la tabla
    x_inicial = 50
    y_inicial = 150
    espaciado = 50
        

    # Dibujar encabezados
    encabezados = ["Pregunta", "Porcentaje de Aciertos"]
    for i, encabezado in enumerate(encabezados):
        texto_encabezado = fuente.render(encabezado, True, WHITE)
        pantalla.blit(texto_encabezado, (x_inicial + i * 500, y_inicial))

    y = y_inicial + espaciado

    # Dibujar filas de estadísticas
    for i, fila in enumerate(estadisticas):
        pregunta = fila[0]
        porcentaje_aciertos = fila[1]

        texto_pregunta = fuente.render(pregunta, True, BLACK)
        texto_porcentaje = fuente.render(f"{porcentaje_aciertos}%", True, BLACK)

        pantalla.blit(texto_pregunta, (x_inicial, y + i * espaciado))
        pantalla.blit(texto_porcentaje, (x_inicial + 600, y + i * espaciado))
    
    

    # Botón para volver al menú
    boton_volver = pygame.Rect(ANCHO // 2 - 100, ALTO - 100, 200, 50)
    pygame.draw.rect(pantalla, RED, boton_volver)
    texto_volver = fuente.render("Salir", True, WHITE)
    pantalla.blit(texto_volver, (ANCHO // 2 - texto_volver.get_width() // 2, ALTO - 90))

    return boton_volver




def mostrar_fallos(pantalla, estadisticas, fuente, ANCHO, ALTO):
    """
    Dibuja el porcentaje de aciertos en la pantalla.
    """
    pantalla.fill(ORANGE)
    titulo = fuente.render("Estadísticas - Fallos", True, WHITE)
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))

        

    # Dibujar encabezados
    encabezados = ["Pregunta", "Fallos"]
    for i, encabezado in enumerate(encabezados):
        texto_encabezado = fuente.render(encabezado, True, WHITE)
        pantalla.blit(texto_encabezado, (x+ i * 600, y))


    # Dibujar filas de estadísticas
    for i, fila in enumerate(estadisticas):
        pregunta = fila[0]
        fallos = fila[1]

        texto_pregunta = fuente.render(pregunta, True, BLACK)
        texto_fallos = fuente.render(f"{fallos}", True, BLACK)

        pantalla.blit(texto_pregunta, (x, y + 50 + i * espaciado))
        pantalla.blit(texto_fallos, (x + 600, y + 50 + i * espaciado))
    
    

    # Botón para volver al menú
    boton_volver = pygame.Rect(ANCHO // 2 - 100, ALTO - 100, 200, 50)
    pygame.draw.rect(pantalla, RED, boton_volver)
    texto_volver = fuente.render("Salir", True, WHITE)
    pantalla.blit(texto_volver, (ANCHO // 2 - texto_volver.get_width() // 2, ALTO - 90))

    return boton_volver



def mostrar_veces_preguntadas(pantalla, estadisticas, fuente, ANCHO, ALTO):
    """
    Dibuja el porcentaje de aciertos en la pantalla.
    """
    pantalla.fill(ORANGE)
    titulo = fuente.render("Estadísticas - Veces Preguntadas", True, WHITE)
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))

        

    # Dibujar encabezados
    encabezados = ["Pregunta", "Veces Preguntadas"]
    for i, encabezado in enumerate(encabezados):
        texto_encabezado = fuente.render(encabezado, True, WHITE)
        pantalla.blit(texto_encabezado, (x+ i * 500, y))


    # Dibujar filas de estadísticas
    for i, fila in enumerate(estadisticas):
        pregunta = fila[0]
        veces_preguntadas = fila[1]

        texto_pregunta = fuente.render(pregunta, True, BLACK)
        texto_veces_preguntadas = fuente.render(f"{veces_preguntadas}", True, BLACK)

        pantalla.blit(texto_pregunta, (x, y + 50 + i * espaciado))
        pantalla.blit(texto_veces_preguntadas, (x + 600, y + 50 + i * espaciado))
    
    

    # Botón para volver al menú
    boton_volver = pygame.Rect(ANCHO // 2 - 100, ALTO - 100, 200, 50)
    pygame.draw.rect(pantalla, RED, boton_volver)
    texto_volver = fuente.render("Salir", True, WHITE)
    pantalla.blit(texto_volver, (ANCHO // 2 - texto_volver.get_width() // 2, ALTO - 90))

    return boton_volver


def mostrar_aciertos(pantalla, estadisticas, fuente, ANCHO, ALTO):
    """
    Dibuja el porcentaje de aciertos en la pantalla.
    """
    pantalla.fill(ORANGE)
    titulo = fuente.render("Estadísticas - Aciertos", True, WHITE)
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))

        

    # Dibujar encabezados
    encabezados = ["Pregunta", "Aciertos"]
    for i, encabezado in enumerate(encabezados):
        texto_encabezado = fuente.render(encabezado, True, WHITE)
        pantalla.blit(texto_encabezado, (x+ i * 500, y))


    # Dibujar filas de estadísticas
    for i, fila in enumerate(estadisticas):
        pregunta = fila[0]
        veces_preguntadas = fila[1]

        texto_pregunta = fuente.render(pregunta, True, BLACK)
        texto_aciertos = fuente.render(f"{veces_preguntadas}", True, BLACK)

        pantalla.blit(texto_pregunta, (x, y + 50 + i * espaciado))
        pantalla.blit(texto_aciertos, (x + 600, y + 50 + i * espaciado))
    
    

    # Botón para volver al menú
    boton_volver = pygame.Rect(ANCHO // 2 - 100, ALTO - 100, 200, 50)
    pygame.draw.rect(pantalla, RED, boton_volver)
    texto_volver = fuente.render("Salir", True, WHITE)
    pantalla.blit(texto_volver, (ANCHO // 2 - texto_volver.get_width() // 2, ALTO - 90))

    return boton_volver
