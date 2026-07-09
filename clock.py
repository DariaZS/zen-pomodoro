'''
clock.py -- all the drawing logic of the clock

Given a canvas, this knows how to draw a face, numerals, real-time 
hands, and (later) the Pomodoro arc. It holds no timer/interval logic --
that lives int timer.py. Painting only.
'''

import math
import tkinter.font as tkfont

# --- colors (migraine-friendly palette) ---
BG = "#1f1f1e"       # charcoal background
FACE = "#2a2a28"     # clock face, a touch lighter
RIM = "#3a3a37"      # outer rim
NUMERAL = "#c9a26b"  # soft gold
HAND = "#89a99a"     # muted sage
FOCUS_ARC = '#89a99a'# sage green - work
BREAK_ARC = "#8C9579" # muted dusty tan - rest

def pick_numeral_font(root):
    '''Pick a playful but readable numeral font from installed fonts'''
    installed = {name.casefold(): name for name in tkfont.families(root)}
    preferred = [
        "Chalkboard SE",
        "Comic Sans MS",
        "Marker Felt",
        "Bradley Hand",
        "Noteworthy",
        "Atkinson Hyperlegible",
        "Arial Rounded MT Bold",
        "Trebuchet MS",
        "Verdana",
    ]

    for family in preferred:
        if family.casefold() in installed:
            return installed[family.casefold()]
    return 'TkDefaultFont'

NUMERALS = ["XII", "I", "II", "III", "IV", "V",
            "VI", "VII", "VIII", "IX", "X", "XI"]


class Clock:
    """Draws a clock face, numerals, and hands onto a given canvas."""

    def __init__(self, canvas, root, size=300):
        # __init__ runs once when we create a Clock. It stores what the
        # clock needs to remember, so other methods can use it later.
        self.canvas = canvas
        self.size = size
        self.center = size // 2
        self.radius = 120
        self.numeral_font = pick_numeral_font(root)

    def draw_face(self):
        """Draw the rim and face — the static background of the clock."""
        c = self.canvas
        cen = self.center
        r = self.radius

        # outer rim
        c.create_oval(
            cen - r - 6, cen - r - 6,
            cen + r + 6, cen + r + 6,
            fill=RIM, outline="",
        )
        # the face
        c.create_oval(
            cen - r, cen - r,
            cen + r, cen + r,
            fill=FACE, outline="",
        )

    def draw_numerals(self):
        """Draw the Roman numerals around the face."""
        c = self.canvas
        cen = self.center
        numeral_radius = self.radius - 22

        for i, roman in enumerate(NUMERALS):
            angle = math.radians(-90 + i * 30)
            x = cen + numeral_radius * math.cos(angle)
            y = cen + numeral_radius * math.sin(angle)
            c.create_text(
                x, y, text=roman,
                fill=NUMERAL, font=(self.numeral_font, 16, "bold"),
            )

    def draw_hands(self):
        '''Draw hour, minute, and second hands at the current real time.'''
        from datetime import datetime

        c = self.canvas
        cen = self.center

        # erase only the hands from the previous tick (tagged 'hands'),
        # leaving the face and numerals untouched
        c.delete('hands')

        now = datetime.now()
        # each hand's fraction around the circle ( 0.0 = 12 o'clock)
        second_f = now.second/60
        minute_f = now.minute/60
        hour_f = (now.hour % 12) / 12 + minute_f / 12

        # helper: draw one hand given it's fraction, length, width, color
        def hand(fraction, length, width, color):
            angle = math.radians(-90 + fraction * 360)
            x = cen + length * math.cos(angle)
            y = cen + length * math.sin(angle)
            c.create_line(
                cen, cen, x, y,
                fill=color, width=width, capstyle="round",
                tags='hands',      # tag so we can erace just the hands
            )


        hand(hour_f,   self.radius - 55, 5, HAND)   # hour: short, thick
        hand(minute_f, self.radius - 30, 3, HAND)   # minute: long, medium
        hand(second_f, self.radius - 20, 1, "#c98b7a")  # second: longest, thin, soft red

        # center hub, drawn last so it sits on top of the hands
        c.create_oval(
            cen - 5, cen - 5, cen + 5, cen + 5,
            fill=HAND, outline='', tags='hands',
        )

    def draw_minute_ticks(self):
        '''Draw 60 small marks around the rim - long hours, shorter between. A classic clockface detail.'''
        c = self.canvas
        cen = self.center

        for i in range(60):
            angle = math.radians(-90 + i * 6)   # 360 / 60 = 6 degrees apart

            if i % 5 == 0:
                inner = self.radius - 10
                width = 2
            else:
                inner = self.radius - 6
                width = 1

            outer = self.radius - 2
            x1 = cen + inner * math.cos(angle)
            y1 = cen + inner * math.sin(angle)
            x2 = cen + outer * math.cos(angle)
            y2 = cen + outer * math.sin(angle)
            c.create_line(x1, y1, x2, y2, fill=NUMERAL, width=width)

    def draw_arc(self, fraction, color):
        '''Draw a soft arc around the rim showing time remaining
        Leaves a small gat at the top so the arc reads as a gauge with
        clear start  and end, rather than an ambiguous full ring.
        fraction 1.0 = nearly full ( with the gap ), 0.0 = nothing left.'''

        c = self.canvas
        cen = self.center
        r = self.radius + 3     # just outside the face

        # erase the previous arc (tagged) so it redraws cleanly each time
        c.delete('arc')

        if fraction <= 0:
            return
        
        gap = 12    # degres of empty space
        max_sweep = 360 - gap   # the fullest the arc ever gets
        sweep = fraction * max_sweep

        start_angle = 90 - gap / 2

        c.create_arc(
            cen - r, cen - r,
            cen + r, cen + r,
            start=start_angle,
            extent=-sweep,  # negative = clockwise
            style='arc', outline=color, width=8,
            tags='arc',
        )

