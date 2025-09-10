import turtle

# Create turtle
t = turtle.Turtle()

# Optional: set speed
t.speed(1)

# Rectangle dimensions
width = 200
height = 100

# Start drawing rectangle
t.down()  # put pen down to start drawing

# Draw rectangle
for _ in range(2):
    t.forward(width)   # draw width
    t.left(90)
    t.forward(height)  # draw height
    t.left(90)

# Finished
turtle.done()

