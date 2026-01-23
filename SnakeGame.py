import random
import os
import time

WIDTH = 20
HEIGHT = 10

def print_board(snake, food):
    os.system("cls" if os.name == "nt" else "clear")
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in snake:
                print("O", end="")
            elif (x, y) == food:
                print("X", end="")
            else:
                print(".", end="")
        print()
    print("Score:", len(snake) - 1)

def move_snake(snake, direction):
    head_x, head_y = snake[0]
    if direction == "w": head_y -= 1
    elif direction == "s": head_y += 1
    elif direction == "a": head_x -= 1
    elif direction == "d": head_x += 1
    new_head = (head_x, head_y)
    return new_head

def main():
    snake = [(WIDTH//2, HEIGHT//2)]
    food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
    direction = "d"

    while True:
        print_board(snake, food)
        move = input("Move (w/a/s/d): ")
        if move in ["w","a","s","d"]:
            direction = move

        new_head = move_snake(snake, direction)

        if (new_head in snake) or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            print("Game Over! Final Score:", len(snake)-1)
            break

        snake.insert(0, new_head)

        if new_head == food:
            food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
        else:
            snake.pop()

        time.sleep(0.1)

main()
