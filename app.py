'''
app.py - the Zen Pomodoro app. This is the file you run

It builds the window, creates the Clock (from clock.py), and wires
everything together. Run it with: python app.py
'''

import tkinter as tk

from clock import BG, BREAK_ARC, FOCUS_ARC, Clock
from timer import PomodoroTimer

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
clock.draw_minute_ticks()
clock.draw_numerals()

# the Pomodoro brain - start it running so it counts down
pomodoro = PomodoroTimer(focus_minutes=25.0, break_minutes=5)
pomodoro.start()


# -- keep the hands updating with real time ---
def tick():
    #print('fraction:', pomodoro.fraction_remaining(), 'phase:', pomodoro.phase)
    if pomodoro.phase == 'focus':
        arc_color = FOCUS_ARC
    else:
        arc_color = BREAK_ARC                     # advance the timer 1 second
    clock.draw_arc(pomodoro.fraction_remaining(), arc_color)   #draw the arc for time left
    clock.draw_hands()                   # real time hands on top
    
    pomodoro.tick() # count down one second, AFTER drawing
    root.after(1000, tick)                  # run again in 1 second

tick()      # start the loop




root.mainloop()