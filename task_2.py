import turtle
import math

def draw_pythagorean_tree(level, length):
    if level == 0:
        turtle.forward(length)
        turtle.backward(length)
        return

    # Draw the trunk
    turtle.forward(length)

    # Draw the left and right branch
    turtle.left(30)
    draw_pythagorean_tree(level - 1, length * math.sqrt(2) / 2)
    turtle.right(30)

    turtle.right(30)
    draw_pythagorean_tree(level - 1, length * math.sqrt(2) / 2)
    turtle.left(30)

    # Move back to the original position
    turtle.backward(length)

# Initial setup
def main():
    turtle.speed('fast')
    turtle.left(90)  # Start pointing up
    turtle.color("green")

    # Get recursion level from user
    level = int(input("Enter the recursion level(type number in range 1-9): "))
    
    # Draw the Pythagorean tree
    draw_pythagorean_tree(level, 150)

    # Complete the drawing
    turtle.done()

if __name__ == "__main__":
    main()