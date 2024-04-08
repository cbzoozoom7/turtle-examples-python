#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl
import random as rand
# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  #t.up()
  c=turtle_colors.pop(0)
  t.fillcolor(c)
  t.pencolor(c)

#  Initialize start position
startx = 0
starty = 0
starth = 0
startpensize = rand.randint(1, 5)

#Moves each turtle to the starting position, turns Southeast, & moves forwards
for t in my_turtles:
  t.goto(startx, starty)
  t.seth(starth)
  t.down()
  t.pensize(startpensize)
  t.forward(rand.randint(20, 100))

#	moves the starting position.
  startx = t.xcor()
  starty = t.ycor()
  starth = t.heading() + rand.randint(30, 60)
  startpensize = t.pensize() + rand.randint(1, 5)

wn = trtl.Screen()
wn.mainloop()