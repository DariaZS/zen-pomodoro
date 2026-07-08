import math
import tkinter as tk

# --- window ---
root = tk.Tk()
root.title('Zen Pomodoro')
root.geometry('360x480')
root.configure(bg='#1f1f1e')

# --- colors (migraine friendly palette) ---
BG = '#1f1f1e'      # charcoal background
FACE = '#2a2a28'    # clock face, a touch lighter
RIM = '#3a3a37'     # outer rim
NUMERAL = '#c9a26b' # soft gold

# --- canvas to draw the clock on ---
SIZE = 300          #canvas is 300x300 pixels
canvas = tk.Canvas(root, width=SIZE, height=SIZE, bg=BG, highlightthickness=0)
canvas.pack(pady=30)    # place it in the window with some space above and below


# --- draw the clock face ---
center = SIZE//2    # 150 - the middle of the canvas
radius = 120        # how big the face is

# outer rim (a slightly bigger circle behind the face)
canvas.create_oval(
    center - radius - 6, center - radius - 6,
    center + radius + 6, center + radius + 6,
    fill=RIM, outline="",
)

# --- the face itself ---
canvas.create_oval(
    center - radius, center - radius,
    center + radius, center + radius,
    fill=FACE, outline="",
)

# --- Roman numerals around the face ---
NUMERALS = ["XII", "I", "II", "III", "IV", "V",
            "VI", "VII", "VIII", "IX", "X", "XI"]

numeral_radius = radius - 22    # a bit inside the rim

for i , roman in enumerate(NUMERALS):
    # each numeral is 30 degrees apart; start at top (-90) and go clockwise
    angle = math.radians(-90 + i * 30)
    x = center + numeral_radius * math.cos(angle)
    y = center + numeral_radius * math.sin(angle)
    canvas.create_text(
        x, y, text = roman,
        #fill = NUMERAL, font=('Georgia', 15, 'bold'),
        fill = NUMERAL, font = ('Baskerville', 15, 'bold'),
    )

# -- the countdown hand (pointing up for now) ---
HAND = "#46b164"    # green light,
HAND_EDGE = "#80d89b"  # subtle lighter edge so the hand pops from the face

hand_length = radius - 45   # a bit shorter than the numeral ring
fraction = 0.0              # 0.0 pointing straight upward ( 1 o'clock)

hand_item = None

def draw_hand_arrow(fraction):
    """Draw a tapered arrow hand that rotates around the center."""
    global hand_item

    angle = math.radians(-90 + fraction * 360)
    ux = math.cos(angle)
    uy = math.sin(angle)

    # Perpendicular unit vector used for hand thickness.
    px = -uy
    py = ux

    tip_x = center + hand_length * ux
    tip_y = center + hand_length * uy

    neck_len = hand_length - 16
    neck_x = center + neck_len * ux
    neck_y = center + neck_len * uy

    tail_len = 12
    tail_x = center - tail_len * ux
    tail_y = center - tail_len * uy

    shaft_half = 3.5
    head_half = 9

    points = [
        tail_x + shaft_half * px, tail_y + shaft_half * py,
        neck_x + head_half * px, neck_y + head_half * py,
        tip_x, tip_y,
        neck_x - head_half * px, neck_y - head_half * py,
        tail_x - shaft_half * px, tail_y - shaft_half * py,
    ]

    if hand_item is not None:
        canvas.delete(hand_item)

    hand_item = canvas.create_polygon(
        points,
        fill=HAND,
        outline=HAND_EDGE,
        width=1,
        joinstyle='round',
    )

draw_hand_arrow(fraction)

# --- center hub ( a little dot covering where the hand meets center)
canvas.create_oval(
    center - 6, center - 6, center + 6, center + 6,
    fill=HAND, outline="",
)

# a variable holding seconds left - start with 25 minutes
remaining = 25 * 60     #15000 seconds
total = 25 * 60         # remember the full amount for the fraction

def tick():
    # this function runs once per second
    global remaining

    # 1. redraw the hand based on how much time has passed
    fraction = 1 - (remaining / total)  # 0.0 at start 1.0 when done
    draw_hand_arrow(fraction)

    # 2. count down
    if remaining > 0:
        remaining -= 1
        root.after(1000, tick) # schedule myself again in 1 second
        






root.mainloop()
