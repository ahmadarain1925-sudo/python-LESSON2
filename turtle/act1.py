import turtle 
turtle.Screen().setup(300,500)
turtle.Screen().bgcolor("pink")
turtle.Screen().title("hexagon")
hexagon=turtle.Turtle ()
sides=6
angles=360/sides
for i in range(sides):
    hexagon.forward (70)
    hexagon.right(angles)
turtle.done()