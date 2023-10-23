"""
Paint: Un sencillo programa de dibujo.

Este programa permite a los usuarios dibujar formas básicas en una ventana utilizando el módulo turtle de Python.
El programa soporta varias formas y colores, y los usuarios pueden interactuar con él a través de clicks del mouse
y atajos de teclado.

Funcionalidades:
1. Dibujar líneas.
2. Dibujar cuadrados.
3. Dibujar círculos (por implementar).
4. Dibujar rectángulos (por implementar).
5. Dibujar triángulos (por implementar).

Atajos de teclado:
- 'u': deshacer.
- 'K': cambiar color a negro.
- 'W': cambiar color a blanco.
- 'G': cambiar color a verde.
- 'B': cambiar color a azul.
- 'R': cambiar color a rojo.
- 'l': seleccionar forma de línea.
- 's': seleccionar forma de cuadrado.
- 'c': seleccionar forma de círculo.
- 'r': seleccionar forma de rectángulo.
- 't': seleccionar forma de triángulo.

Módulos:
- turtle: para dibujar y manejar la ventana gráfica.
- freegames.vector: para manejar vectores 2D.

Ejercicios sugeridos:
1. Añadir un color.
2. Completar la función de círculo.
3. Completar la función de rectángulo.
4. Completar la función de triángulo.
5. Añadir parámetro de ancho.

Fernando A01642285
Diego A01026512
Federico A01660986

Actividad 1. Juego Pintando

"""

from turtle import *
from freegames import vector

def line(start, end):
    """
    Dibuja una línea desde el punto de inicio hasta el punto final.
    
    Parámetros:
    - start: vector, punto de inicio.
    - end: vector, punto final.
    """
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    """
    Dibuja un cuadrado usando el punto de inicio como esquina superior izquierda 
    y el punto final como esquina inferior derecha.
    
    Parámetros:
    - start: vector, punto de inicio.
    - end: vector, punto final.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Las siguientes funciones (circle, rectangle, triangle) están por implementar.

def circle(start, end):
    """Dibuja un círculo desde el punto de inicio hasta el punto final."""
    pass

def rectangle(start, end):
    """Dibuja un rectángulo desde el punto de inicio hasta el punto final."""
    pass

def triangle(start, end):
    """Dibuja un triángulo desde el punto de inicio hasta el punto final."""
    pass

def tap(x, y):
    """
    Almacena el punto de inicio o dibuja la forma seleccionada.
    Si es el primer click, se almacena el punto de inicio. 
    Si es el segundo click, se dibuja la forma y se reinicia el punto de inicio.
    
    Parámetros:
    - x: int, coordenada x del click.
    - y: int, coordenada y del click.
    """
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """
    Almacena un valor en el diccionario de estado.
    
    Parámetros:
    - key: str, clave para el valor.
    - value: valor a almacenar.
    """
    state[key] = value

# Inicialización y configuración del programa.
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
