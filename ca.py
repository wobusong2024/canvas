# import tkinter as tk
# root = tk.Tk()
# root.title("canvas ainimation")
# canvas = tk.Canvas(
#     root,
#     width=600,
#     height=350,
#     bg="white"
    
# )
# canvas.pack()

# ball = canvas.create_oval(
#     40,40,90,90,
#     fill="purple",
#     outline=""
# )
# def move_ball():
#     canvas.move(ball,5,0)
#     root.after(30,move_ball)
  

# move_ball()
# root.mainloop()


import tkinter as tk

root = tk.Tk()
root.title("Bouncing Ball")

canvas = tk.Canvas(
    root,
    width=600,
    height=350,
    bg="white"
)
canvas.pack()

# Create the ball
ball = canvas.create_oval(
    20, 20, 70, 70,
    fill="orange",
    outline=""
)

# Set the initial speed
dx = 3
dy = 0
gravity = 0.5
bounce_speed = -10

ground = 300
bounces = 0

def animate():
    global dx, dy, bounce_speed, bounces

    x1, y1, x2, y2 = canvas.coords(ball)

    # Apply gravity
    dy += gravity

    # Move the ball
    canvas.move(ball, dx, dy)

    x1, y1, x2, y2 = canvas.coords(ball)

    # Bounce when the ball reaches the ground
    if y2 >= ground:
        canvas.coords(ball, x1, ground - 50, x2, ground)
        bounces += 1

        # Stop after the bounces become very small
        if abs(bounce_speed) < 3 or bounces >= 6:
            return

        # Reduce the bounce height and speed
        dy = bounce_speed
        bounce_speed *= 0.65

    # Continue animation
    root.after(20, animate)

animate()
root.mainloop()