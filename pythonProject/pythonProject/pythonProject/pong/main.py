from time import *
from ball import *
from paddle import *
from score import *

screen = Screen()
screen.tracer(0)
r_paddle = Paddle((280, 0))
l_paddle = Paddle((-280, 0))
ball = Ball()
score=Score()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    ball.mov()

    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_wall()
    if ball.distance(r_paddle) < 45 and ball.xcor() > 250 or ball.distance(l_paddle) < 45 and ball.xcor() < -250:
        ball.bounce_paddle()
    if ball.xcor() > 280:
        ball.ball_reset()
        score.l_point()
    if ball.xcor() < -280:
        ball.ball_reset()
        score.r_point()
screen.exitonclick()
