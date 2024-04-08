#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider is used
spider = trtl.Turtle()
#create a spider body
spider.pensize(40)
spider.circle(20)
#configure legs
numLegs = 6
legLength = 70
angleBetweenLegs = 380 / numLegs
#draw legs
spider.pensize(5)
legsDrawn = 0
while (legsDrawn < numLegs):
  spider.goto(0,0)
  spider.setheading(angleBetweenLegs*legsDrawn)
  spider.forward(legLength)
  legsDrawn = legsDrawn + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()