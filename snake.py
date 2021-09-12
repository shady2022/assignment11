import arcade
import random

class Object():
    def __init__(self, w, h):
        self.center_x = random.randint(20, w - 20)
        self.center_y = random.randint(20, h - 20)
        
        
        
class Apple(arcade.Sprite , Object):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        Object.__init__(self, w, h)
        self.img = arcade.Sprite(':resources:images/tiles/mushroomRed.png')
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y
        self.color = arcade.color.RED_DEVIL
        self.r = 10
        
    def draw(self):
        self.img.draw()
        
        
class Pear(arcade.Sprite , Object):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        Object.__init__(self, w, h)
        self.img = arcade.Sprite(':resources:images/enemies/fishPink.png')
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y

    def draw(self):
        self.img.draw()
        
        
class Lol(arcade.Sprite , Object):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        Object.__init__(self, w, h)
        self.img = arcade.Sprite(':resources:images/enemies/fly.png')
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y
        
    def draw(self):
        self.img.draw()
        

class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color1 = arcade.color.ARMY_GREEN
        self.color2 = arcade.color.APPLE_GREEN
        self.speed = 5
        self.r = 8
        self.center_x = w // 2
        self.center_y = h // 2
        
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.flag = 0
        self.body = []
        self.body.append([self.center_x,self.center_y])
        
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color1)

        for index, item in enumerate(self.body):
            if index % 2 == 0:
                arcade.draw_circle_filled(item[0], item[1], self.r, self.color2)
            else:
                arcade.draw_circle_filled(item[0], item[1], self.r, self.color1)



    def move(self):
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
        
        self.body.append([self.center_x, self.center_y])
        if self.flag == 0:
            del(self.body[0])

        
    def Eat(self, fruit):
        if fruit == 'apple':
            self.score += 1

        if fruit == 'pear':
            self.score += 2

        if fruit == 'lol':
            self.score -= 1
    
   

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, width, height, 'snake')
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(width, height)
        self.apple = Apple(width, height)
        self.pear = Pear(width, height)
        self.lol = Lol(width, height)
        self.flag = 0
        self.exit = 0
            
    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.lol.draw()
        
        output = f"Score: {self.snake.score}"
        arcade.draw_text(output, 10, 20, arcade.color.DARK_BLUE_GRAY, 14)
        
        if self.snake.score != 0:
            self.flag = 1

        if self.flag == 1:
            if self.snake.score <= 0:
                arcade.draw_text("Game Over", 230, 200, arcade.color.DARK_BLUE_GRAY, 20)
                self.exit = 1
                
                
        if (600 <= self.snake.center_x + self.snake.r) or (0 >= self.snake.center_x - self.snake.r) or (400 <= self.snake.center_y + self.snake.r) or (0 >= self.snake.center_y - self.snake.r):
            arcade.draw_text("Game Over", 230, 200, arcade.color.DARK_BLUE_GRAY, 20)
            self.exit = 1

    def on_update(self, delta_time: float):
        self.snake.move()
        self.snake.flag = 0
        if self.apple.center_x - 10 <= self.snake.center_x <= self.apple.center_x + 10 and self.apple.center_y - 10 <= self.snake.center_y <= self.apple.center_y + 10 :
            fruit = 'apple'
            self.snake.Eat(fruit)
            self.apple = Apple(60, 40)

        if self.pear.center_x - 10 <= self.snake.center_x <= self.pear.center_x + 10 and self.pear.center_y - 10 <= self.snake.center_y <= self.pear.center_y + 10 :
            fruit = 'pear'
            self.snake.Eat(fruit)
            self.pear = Pear(60, 40)

        if self.lol.center_x - 10 <= self.snake.center_x <= self.lol.center_x + 10 and self.lol.center_y - 10 <= self.snake.center_y <= self.lol.center_y + 10 :
            fruit = 'lol'
            self.snake.Eat(fruit)
            self.lol = Lol(60, 40)
                
        
    def on_key_release(self, Key, modifiers):
        
        if Key == arcade.key.W:
            self.snake.change_y = 1
            self.snake.change_x = 0
            
        elif Key == arcade.key.S:
            self.snake.change_y = -1
            self.snake.change_x = 0
            
        elif Key == arcade.key.A:
            self.snake.change_y = 0
            self.snake.change_x = -1    
            
        elif Key == arcade.key.D:
            self.snake.change_y = 0
            self.snake.change_x = 1 
            
         
            
            
    
            
width =800
height = 600           
game = Game(width,height)
arcade.run()
        