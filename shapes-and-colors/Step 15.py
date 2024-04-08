#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  t.up()
  c=turtle_colors.pop(0)
  t.fillcolor(c)
  t.pencolor(c)

#  Initialize start position
startx = 0
starty = 0
starth = -45

#Moves each turtle to the starting position, turns Southeast, & moves forwards
for t in my_turtles:
  t.goto(startx, starty)
  t.seth(starth)
  t.down()
  t.forward(50)

#	moves the starting position.
  startx = t.xcor()
  starty = t.ycor()
  starth = t.heading() - 45

wn = trtl.Screen()
wn.mainloop()