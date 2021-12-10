import time
import arcade
import random
#######golabi#######
class Golabi(arcade.Sprite):

    def __init__(self, w, h):

        arcade.Sprite.__init__(self)
        self.img = 'golabi.jpg'
        self.golabi = arcade.Sprite(self.img , 0.02)

        self.golabi.center_x = random.randint(0, w)

        self.golabi.center_y = random.randint(0, h)

    def draw(self):

        self.golabi.draw()
#########poop#########

class Poop(arcade.Sprite):

    def __init__(self, w, h):

        arcade.Sprite.__init__(self)

        self.img = 'poop.jpg'

        self.p = arcade.Sprite(self.img , 0.04)

        self.p.center_x = random.randint(0, w)

        self.p.center_y = random.randint(0, h)

    def draw(self):

        self.p.draw()     
#######sib########           

class Sib(arcade.Sprite):

    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.img = 'sib.jpg'
        self.sib = arcade.Sprite(self.img , 0.04)

        self.sib.center_x = random.randint(0, w)

        self.sib.center_y = random.randint(0, h)

    def draw(self):
        self.sib.draw()
##########snake########
        
class Snake(arcade.Sprite):

    def __init__(self, w, h):

        arcade.Sprite.__init__(self)


        self.color = arcade.color.PURPLE
        self.speed = 2

        self.width = 20

        self.height = 20

        self.center_x = w // 2

        self.center_y = h // 2

        self.r = 7

        self.change_x = 0

        self.change_y = 0

        self.score = 0

        self.body = []
        self.body.append([self.center_x, self.center_y])

    def draw(self):        
        for i in range(len(self.body)):
            if i % 3 == 0:
                arcade.draw_circle_filled(self.body[i][0], self.body[i][1], self.r, self.color)

            elif i % 3 == 1:
                arcade.draw_circle_filled(self.body[i][0], self.body[i][1], self.r, arcade.color.YELLOW)

            else:
                arcade.draw_circle_filled(self.body[i][0], self.body[i][1], self.r, arcade.color.RED)
       
    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y


    def khordan(self , n):

        if n == 'sib':
            self.score += 1

        elif n == 'golabi':
            self.score += 2

        elif n == 'poop':

            self.score -= 1   
###########game##########
class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 600, 500, 'welcome to snake game!')
        arcade.set_background_color(arcade.color.GREEN)

        self.snake = Snake(600, 500)
        self.sib = Sib(600, 500)
        self.golabi = Golabi(600, 500)
        self.poop = Poop(600, 500)

    def on_draw(self):
       
        arcade.start_render()
        if self.snake.center_x <= 0 or self.snake.center_x >= 600 \
            or self.snake.center_y <= 0 or self.snake.center_y >= 500 \
                or self.snake.score < 0 :
            
            arcade.draw_text('Game Over', start_x= 120, start_y= 250,   
                color= arcade.color.BLACK, font_size = 40)
            arcade.exit()
        else:
            self.snake.draw()

            self.sib.draw()

            self.golabi.draw()

            self.poop.draw()

            arcade.draw_text('Score: %i'%self.snake.score, start_x= 250, start_y= 10,

            color= arcade.color.BLUE, font_size = 14)

    def on_update(self, delta_time: float):
        

        self.snake.move()

        if arcade.check_for_collision(self.snake, self.sib.sib):

            self.snake.khordan('sib')
            self.snake.body.append([self.snake.body[len(self.snake.body)-1][0],

             self.snake.body[len(self.snake.body)-1][1]])

            self.sib = Sib(600, 500)

        elif arcade.check_for_collision(self.snake, self.golabi.golabi):

            self.snake.khordan('golabi')

            self.snake.body.append([self.snake.body[len(self.snake.body)-1][0],

             self.snake.body[len(self.snake.body)-1][1]])

            self.golabi = Golabi(600, 500)

        elif arcade.check_for_collision(self.snake, self.poop.p):

            self.snake.khordan('poop')
            self.poop = Poop(600, 500)

    def on_key_release(self, key, modifiers):
    

        if key == arcade.key.UP:

            self.snake.change_x = 0
            self.snake.change_y = +1
        
        elif key == arcade.key.DOWN:

            self.snake.change_x = 0
            self.snake.change_y = -1
        elif key == arcade.key.LEFT:

            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT:

            self.snake.change_x = +1
            self.snake.change_y = 0    

game = Game()

arcade.run()

        