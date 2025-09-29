import turtle

import turtle
import time
class Enjoy:
    def __init__(self):
        print(f"draw geometry")
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Line")

        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.pensize(3)
        self.turtle.color("darkgreen")
        self.turtle.speed(1)
        self.turtle.fillcolor("red")
    
    def draw_cube(self):
        try:
            size = 100
            angle = 30

            for _ in range(4):
                self.turtle.forward(size)
                self.turtle.left(90)

            self.turtle.goto(0,0)
            self.turtle.setheading(angle)
            self.turtle.forward(size)
            self.turtle.right(90 + angle)

            for _ in range(4):
                self.turtle.forward(size)
                self.turtle.right(90)
            
        except Exception as e:
            raise e
        
    def draw_pyramid(self):
        try:
            size = 100
            for _ in range(4):
                self.turtle.forward(size)
                self.turtle.left(90)

            self.turtle.goto(50, 50)

            corners = [(0,0), (100, 0), (100,100), (0, 100)]
            for x, y in corners:
                self.turtle.goto(x, y)
                self.turtle.goto(50,50)
        except Exception as e:
            raise e
        
    def stacked_cubes(self):
        try:
            size = 100
            angle = 30

            for _ in range(4):
                self.turtle.forward(size)
                self.turtle.right(90)

            self.turtle.goto(0, 0)

            corners = [(0,0), (100,0), (100,-100)]
            for x, y in corners:
                self.turtle.goto(x, y)
                self.turtle.goto(0, 0)
        except Exception as e:
            raise e
        

def main():
    try:
        enj = Enjoy()
        # enj.draw_cube()
        # enj.draw_pyramid()
        enj.stacked_cubes()

    except Exception as e:
        print(f"Failed: {e}")
    finally:
        # turtle.done()
        # turtle.Screen().mainloop()
        turtle.Screen().exitonclick()

if __name__ == "__main__":
    main()