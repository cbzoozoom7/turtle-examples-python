#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
import random as rand
wn = trtl.Screen()
# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []
collision_radius = 20
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
collision_shape = "triangle"
tloc = 50
for s in turtle_shapes:

	ht = trtl.Turtle(shape=s)
	horiz_turtles.append(ht)
	ht.penup()
	new_color = horiz_colors.pop()
	ht.fillcolor(new_color)
	ht.goto(-350, tloc)
	ht.setheading(0)

	vt = trtl.Turtle(shape=s)
	vert_turtles.append(vt)
	vt.penup()
	new_color = vert_colors.pop()
	vt.fillcolor(new_color)
	vt.goto( -tloc, 350)
	vt.setheading(270)
	
	tloc += 50
turtle_lists = (horiz_turtles, vert_turtles)
#move turtles across and down screen, stopping for collisions
collision_color = "red"
for steps in range(30):
	for active_list in turtle_lists:
		inactive_lists = list(turtle_lists)
		inactive_lists.remove(active_list)
		for t in active_list:
			dist = rand.randint(1, 50)
			if (((t.xcor() + dist) < ((wn.screensize()[0] / 2) - 10)) and (((t.ycor() - dist) > (-((wn.screensize()[1] / 2) - 10))))):
				t.forward(dist)
				for inactive in inactive_lists:
					for c in inactive:
						if (((abs(t.xcor() - c.xcor())) <= collision_radius) and (abs(t.ycor() - c.ycor()) <= collision_radius)):
							t.shape(collision_shape)
							c.shape(collision_shape)
							t.fillcolor(collision_color)
							c.fillcolor(collision_color)
							active_list.remove(t)
							inactive.remove(c)
for active_list in turtle_lists:
	for t in active_list:
		t.fillcolor("gray")
wn.mainloop()
