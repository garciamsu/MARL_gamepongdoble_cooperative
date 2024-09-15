import turtle
import random

class Game:
    def __init__(self):
        # Configuración de la ventana del juego
        self.window = turtle.Screen()
        self.window.title("Pong Game Cooperativo")
        self.window.bgcolor("lightgreen")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        # Crear instancias de las clases anidadas
        self.paddle_a = self.Paddle(350, 50, "blue")
        self.paddle_b = self.Paddle(350, -50, "red")
        self.ball = self.Ball()
        self.scoreboard = self.Scoreboard()

        # Configuración de controles
        self.window.listen()
        self.window.onkeypress(self.paddle_a.move_up, "Up")
        self.window.onkeypress(self.paddle_a.move_down, "Down")
        self.window.onkeypress(self.paddle_b.move_up, "w")
        self.window.onkeypress(self.paddle_b.move_down, "s")

        # Iniciar el juego
        self.run_game()

    class Paddle(turtle.Turtle):
        def __init__(self, x, y, color):
            super().__init__()
            self.shape("square")
            self.color(color)
            self.shapesize(stretch_wid=6, stretch_len=1)
            self.penup()
            self.goto(x, y)

        def move_up(self):
            y = self.ycor()
            if y < 250:
                self.sety(y + 20)

        def move_down(self):
            y = self.ycor()
            if y > -240:
                self.sety(y - 20)

    class Ball(turtle.Turtle):
        def __init__(self):
            super().__init__()
            self.shape("circle")
            self.color("white")
            self.penup()
            self.goto(0, 0)
            self.dx = random.choice([-0.2, -0.15])
            self.dy = random.choice([-0.2, 0.2])

        def move(self):
            self.setx(self.xcor() + self.dx)
            self.sety(self.ycor() + self.dy)

            return "continue"

        def bounce_y(self):
            self.dy *= -1
            # Variar velocidad tras cada rebote
            #self.dy += random.choice([0.01, -0.01])

        def bounce_x(self):
            self.dx *= -1
            # Variar velocidad tras cada rebote
            #self.dx += random.choice([0.01, -0.01])

    class Scoreboard(turtle.Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.color("black")
            self.penup()
            self.hideturtle()
            self.goto(0, 260)
            self.update_score()

        def update_score(self):
            self.clear()
            self.write(f"Puntuación: {self.score}", align="center", font=("Courier", 24, "normal"))

        def increase_score(self):
            self.score += 1
            self.update_score()

    def check_collisions(self):
        
        print(self.ball.ycor())
        # Rebote en el borde lateral izquierdo
        if self.ball.xcor() <= -280:
            self.ball.setx(280)
            self.ball.bounce_x()

        # Rebote en los bordes inferior o superior
        if self.ball.ycor() >= 280 or self.ball.ycor() <= -280:
            self.ball.bounce_y()
           
        # Rebote en la paleta
        #if (-260 <= self.ball.ycor() <= -230) and \
        #   (self.agent.paddle.xcor() - 50 <= self.ball.xcor() <= self.agent.paddle.xcor() + 50):
        #    self.ball.sety(-230)
        #    self.ball.bounce_y()
        #    self.score += 10
        #    self.plays += 1
        #    self.show_score()

        # Revisar si la pelota toca el borde inferior
        #if self.ball.ycor() <= -280:
            #self.ball.reset_position()
            #self.score -= 10
            #self.plays += 1
            #self.agent.lives -= 1
            #self.show_score()

    def run_game(self):
        while True:
            self.window.update()

            # Mover la pelota
            status = self.ball.move()

            # Chequea las colisiones
            self.check_collisions()

            # Revisar si la pelota fue fallada
            if status == "missed":
                break  # El juego termina si la pelota es fallada

        # Finaliza el juego
        self.window.bye()

# Iniciar el juego
if __name__ == "__main__":
    Game()
