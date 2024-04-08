#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider is used
spider = trtl.Turtle()
#create a spider body
spider.pensize(40)
spider.circle(20)
#configure legs
numLegs = 8
legLength = 70
angleBetweenLegs = 270 / numLegs
#draw legs
spider.pensize(5)
for side in range(2):
  legsDrawn = 0
  while (legsDrawn < (numLegs / 2)):
    spider.goto(0,20)
    spider.setheading((angleBetweenLegs*legsDrawn) + (180 * side))
    spider.forward(legLength)
    legsDrawn = legsDrawn + 1
#draw eyes
spider.up()
spider.goto(-20,30)
spider.pencolor("red")
spider.dot(5)
spider.goto(-15, 37)
spider.dot(5)
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()