from tkinter import *

master = Tk()

w = Canvas(master, width=400, height=400)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

w.create_rectangle(30, 10, 120, 80, outline="#fb0", fill="#fb0")
w.create_rectangle(150, 10, 240, 80, outline="#f50", fill="#f50")
w.create_rectangle(270, 10, 370, 80, outline="#05f", fill="#05f")


w.create_oval(10, 10, 80, 80, outline="gray",  fill="gray", width=2)
w.create_oval(110, 10, 210, 80, outline="gray",         fill="gray", width=2)
w.create_rectangle(230, 10, 290, 60,  outline="gray", fill="gray", width=2)
w.create_arc(30, 200, 90, 100, start=0, extent=210, outline="gray", fill="gray", width=2)

w.create_text(30, 290, anchor=W, text="Somebody tell me why I'm here")
            
points = [150, 100, 200, 120, 240, 180, 210,  200, 150, 150, 100, 200]
w.create_polygon(points, outline='gray', fill='gray', width=2)        

mainloop()
