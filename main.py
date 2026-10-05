# import tkinter as tk

# root = tk.Tk()
# root. title("My First Canvas")

# canvas= tk.Canvas (root, width=500,
# height=350, bg="white")

# canvas.pack()

# canvas.create_rectangle (40, 40, 220, 150, fill="purple") 
# canvas.create_oval(280, 50, 440, 190, fill="lightblue") 
# canvas.create_line(50, 250, 300, 250, width=4) 
# canvas.create_text(275, 310, text="Hello Canvas", font= ("Arial", 20))

# root.mainloop()


import tkinter as tk


root = tk.Tk()
root.title("Zams House")


canvas = tk.Canvas(root, width=500, height=400, bg="skyblue")
canvas.pack()

canvas.create_rectangle(120, 150, 380, 320, fill="lightyellow", outline="black")
canvas.create_polygon(100, 150, 250, 50, 400, 150, fill="brown", outline="black")
canvas.create_rectangle(150, 180, 200, 230, fill="lightblue", outline="black")
canvas.create_rectangle(300, 180, 350, 230, fill="lightblue", outline="black")
canvas.create_rectangle(220, 220, 280, 320, fill="pink", outline="black")



root.mainloop()
