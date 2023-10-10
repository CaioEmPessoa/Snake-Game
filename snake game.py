import random
import time

class SnakeGame():

    def __init__(self):
        super().__init__()
        self.field = []
        self.size = range(5)
        self.grass = " 🌳 "
        self.snake = " 🐍 "
        self.apple = " 🍎 "
        self.points = 0
        self.head_y = 2
        self.head_x = 2

        self.body = []


        for i in self.size:
            self.field.append([self.grass for i in self.size])

        self.field[self.head_y][self.head_x] = self.snake

    def change_apple(self):
        self.apple_x = random.choice(self.size)
        self.apple_y = random.choice(self.size)
        
        if self.apple_x != self.head_x or self.apple_y != self.head_y:
            self.field[self.apple_y][self.apple_x] = self.apple
        else:
            self.change_apple()
            return

    def show_field(self):
        print(f"==== ==== {str(self.points)} ==== ====")
        for square in self.field:
            print("".join(square))

    def move_snake(self):
        while True:
            self.snake_dir = input("Pra onde ela vai?\n")
                
            self.field[self.head_y][self.head_x] = self.grass

            match self.snake_dir:
                case "w":
                    self.head_y-=1
                case "s":
                    self.head_y+=1
                case "d":
                    self.head_x+=1
                case "a":
                    self.head_x-=1
                case __:
                    break
                
            # if snake gets out of map
            if self.head_x >= len(self.size) or self.head_y >= len(self.size) or self.head_x == -1 or self.head_y == -1:
                break

            if self.head_x == self.apple_x and self.head_y == self.apple_y:
                self.points += 1
                print(self.body)

                self.change_apple()

            self.field[self.head_y][self.head_x] = self.snake

            self.show_field()

        print("o jogo acabou. receba seu doce messinho.")

    def start(self):
        self.change_apple()
        self.show_field()
        self.move_snake()

game = SnakeGame()
game.start()


