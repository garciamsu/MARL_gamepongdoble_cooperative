from math import ceil, floor
import turtle
import time
import numpy as np

import turtle

# Configuración de la ventana
window = turtle.Screen()
window.title("Pong Cooperativo")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Marcador
score = 0

# Pala base
class Paddle(turtle.Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(x_position, y_position)

    def move_up(self):
        y = self.ycor()
        if y < 250:  # Limitar el movimiento para que no salga de la pantalla
            self.sety(y + 20)

    def move_down(self):
        y = self.ycor()
        if y > -240:  # Limitar el movimiento para que no salga de la pantalla
            self.sety(y - 20)

# Pelota
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.15
        self.dy = 0.15

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

# Dibujar el marcador
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Puntaje: 0", align="center", font=("Courier", 24, "normal"))

    def update_score(self, score):
        self.clear()
        self.write(f"Puntaje: {score}", align="center", font=("Courier", 24, "normal"))

# Inicializar palas (ambas en el lado derecho), pelota y marcador
right_paddle_1 = Paddle(350, 100)  # Primera pala del lado derecho
right_paddle_2 = Paddle(350, -100) # Segunda pala del lado derecho
ball = Ball()
scoreboard = Scoreboard()

# Controles del teclado
window.listen()
window.onkeypress(right_paddle_1.move_up, "Up")
window.onkeypress(right_paddle_1.move_down, "Down")
window.onkeypress(right_paddle_2.move_up, "w")
window.onkeypress(right_paddle_2.move_down, "s")

# Bucle principal del juego
while True:
    window.update()

    # Movimiento de la pelota
    ball.move()

    # Rebote en el borde superior e inferior
    if ball.ycor() > 290:
        ball.sety(290)
        ball.bounce_y()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.bounce_y()

    # Rebote en las palas cooperativas del lado derecho
    if (ball.dx > 0 and ball.xcor() > 340 and (ball.distance(right_paddle_1) < 50 or ball.distance(right_paddle_2) < 50)):
        ball.bounce_x()

    # Verificar si la pelota sale del lado izquierdo (anota un punto)
    if ball.xcor() > 390:
        score -= 1  # Pierden puntos si la pelota pasa por el lado derecho
        scoreboard.update_score(score)
        ball.reset_position()

    # Verificar si la pelota pasa por el lado izquierdo (anotan un punto)
    if ball.xcor() < -390:
        score += 1  # Ganan puntos si la pelota sale por el lado izquierdo
        scoreboard.update_score(score)
        ball.reset_position()
