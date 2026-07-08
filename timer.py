'''
timer.py - Pomodoro interval logic. Pure state, no drowing.

Tracks the current phase (focus or break), how long each lasts,
and how much time is left. Knows how to tick down and switch phases in a loop.
It answers questions; app.py asks them and tells clock.py what to draw.
'''

class PomodoroTimer:
    '''Tracks focus/break phases and counts them down.'''

    def __init__(self, focus_minutes=25, break_minutes=5):
        self.focus_seconds = focus_minutes * 60
        self.break_seconds = break_minutes * 60

        self.phase = 'focus'
        self.remaining = self.focus_seconds
        self.running = False

    def total_for_phase(self):
        '''How many seconds the current phase lasts in full.'''
        if self.phase == "focus":
            return self.focus_seconds
        return self.break_seconds
    
    def fraction_remaining(self):
        '''How much of the current phase is left, as 0.0-1.0.
        Used later to draw the shrinking arc.'''
        total = self.total_for_phase()
        if total == 0:
            return 0.0
        return self.remaining / total
    
    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def tick(self):
        '''Advance one second. returns True if the phase
        just switched.'''
        if not self.running:
            return False
        
        if self.remaining > 0:
            self.remaining -= 1
            return False
        
        #phase is over -- switch to the other phase and reset its clock
        self._switch_phase()
        return True
    
    def _switch_phase(self):
        '''Flip focus <-> break and reset remaining time'''
        if self.phase == 'focus':
            self.phase = 'break'
            self.remaining = self.break_seconds
        else:
            self.phase = 'focus'
            self.remaining = self.focus_seconds