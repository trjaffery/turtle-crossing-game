import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# TODO: #1 - Create the turtle and allow it to move

turtle = Player()

screen.listen()

screen.onkey(key="Up", fun=turtle.move)

# TODO: #2 - Create the cars and their behavior
carManager = CarManager()

scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.spawn_car()
    carManager.car_move()
    scoreboard.write_level()

    # TODO: #3 - Detect when a car collides with the turtle

    for car in carManager.cars:
        car_y = car.ycor()
        player_y = turtle.ycor()
        abs_y = abs(car_y - player_y)
        # No need to measure the player as we know it is always at X = 0
        abs_x = abs(car.xcor())
        if abs_y < 18 and abs_x <= 20:
            game_is_on = False
            scoreboard.game_over()
    # for car in carManager.cars:
    #     if turtle.distance(car) < 20:
    #         game_is_on = False

    # TODO: #4 - Detect when the turtle makes it to the finish line - Scoreboard/Level

    if turtle.reached_finish_line():
        scoreboard.update_level()
        carManager.new_level()

screen.exitonclick()
