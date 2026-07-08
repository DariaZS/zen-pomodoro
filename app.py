'''
app.py - the Zen Pomodoro app. This is the file you run

It builds the window, creates the Clock (from clock.py), and wires
everything together. Run it with: python app.py
'''

import tkinter as tk

from clock import BG, Clock

# --- window ---
root = tk.Tk()
root.title('Zen Pomodoro')
root.geometry('360x480')
root.configure(bg=BG)

# --- canvas for the clock to draw on ---
SIZE = 300
canvas = tk.Canvas(root, width=SIZE, height=SIZE, bg=BG, highlightthickness=0)
canvas.pack(pady=30)

# --- create the clock and draw it ---
clock = Clock(canvas, root, size=SIZE)
clock.draw_face()
clock.draw_numerals()

# -- keep the hands updating with real time ---
def tick():
    clock.draw_hands()
    root.after(1000, tick)     # run again in 1 second

tick()      # start the loop




root.mainloop()