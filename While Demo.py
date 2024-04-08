#   a113_long_circle.py
#   Draw a circle calling only the forward and
#   right methods
import turtle as trtl

painter = trtl.Turtle()
for a in range(18):
# Your code here
  painter.forward(20)
  painter.right(20)
wn = trtl.Screen()
wn.mainloop()