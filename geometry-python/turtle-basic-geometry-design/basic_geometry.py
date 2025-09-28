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
        self.turtle.speed(4)
        self.turtle.fillcolor("red")
    
    def draw_line(self):
        try:
            self.turtle.forward(100)
        except Exception as e:
            raise e

    def draw_square(self):
        try:
            for _ in range(4):
                self.turtle.forward(100)
                self.turtle.right(90)
        except Exception as e:
            raise e
        
    def draw_triangle(self):
        try:
            self.turtle.begin_fill()
            for _ in range(3):
                self.turtle.forward(100)
                self.turtle.left(120)
            self.turtle.end_fill()
        except Exception as e:
            raise e
        
    def draw_circle(self):
        try:
            self.turtle.circle(80)
        except Exception as e:
            raise e
    
    def draw_rectangle(self):
        try:
            for _ in range(2):
                self.turtle.forward(200)
                self.turtle.right(90)
                self.turtle.forward(100)
                self.turtle.right(90)
        except Exception as e:
            raise e
        
    def draw_pentagon(self):
        try:
            ext_angle = 360 / 5
            for _ in range(5):
                self.turtle.forward(100)
                self.turtle.right(ext_angle)
        except Exception as e:
            raise e
        
    def draw_decagon(self):
        try:
            ext_angle = 360/10
            for _ in range(10):
                self.turtle.forward(50)
                self.turtle.right(ext_angle)
        except Exception as e:
            raise e
        
        
def main():
    try:
        enj = Enjoy()
        # enj.draw_line()
        # enj.draw_square()
        # enj.draw_triangle()
        # enj.draw_circle()
        # enj.draw_rectangle()
        # enj.draw_pentagon()
        enj.draw_decagon()

    except Exception as e:
        print(f"Failed: {e}")
    finally:
        # turtle.done()
        # turtle.Screen().mainloop()
        turtle.Screen().exitonclick()

if __name__ == "__main__":
    main()