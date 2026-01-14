import turtle

# Recursion function for edge creation
def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_edge(length, depth - 1)
        turtle.left(60)
        draw_edge(length, depth - 1)
        turtle.right(120)   
        draw_edge(length, depth - 1)
        turtle.left(60)
        draw_edge(length, depth - 1)

# Function for drawing polygon 
def draw_polygon(sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.left(angle)
 
sides = int(input("Enter  number of sides: ")) # input for number of sides
length = int(input("Enter side length: ")) # input for length of sides (in pixels)
depth = int(input("Enter recursion depth: ")) # input that specifies the depth of recursion

# turtle setup
turtle.speed(0)
turtle.hideturtle()

# calling function by giving values
draw_polygon(sides, length, depth)
turtle.done()