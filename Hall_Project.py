import turtle as trtl
import random as rand

g = trtl.Turtle()
g.speed(0)

random_stuff_x = rand.randint(-200,200)
random_stuff_y = rand.randint(-150,150)



def ghost():
  g.hideturtle()
  g.penup()
  g.goto(random_stuff_x,random_stuff_y)

      



def candy():
  Candy_corn = "Candy_corn.png"
  wn.addshape(Candy_corn)

candy()

wn = trtl.Screen()
wn.mainloop()
