import turtle

def colores():
    # Introducimos el color de la estrella:
    turtle.color('black')           # (Color del puntero)
    turtle.begin_fill()             # (Comenzamos a rellenar)
    turtle.fillcolor("#FF99FF")     # (Color del relleno)

    # Elegimos el grosor de la estrella:
    turtle.width(3)

    # Introducimos el color del fondo de la ventana:
    turtle.bgcolor('white')


def coordenadas():
    # Introducimos las coordenadas de la estrella:
    turtle.setx(-250)


def estrella():
    while True:
        # Marcamos el movimiento y el giro de la estrella:
        turtle.forward(500)              # (Movimiento)
        turtle.right(160)                # (Giro)

        # Si volvemos al punto de partida, la estrella se ha completado:
        if turtle.heading() == 0:
            turtle.end_fill()               # (Terminamos de rellenar)
            turtle.done()





