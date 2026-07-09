## Build order (small steps, each runnable)

1. [x] Empty window appears
2. [x] Draw a static clock face (rim, face, Roman numerals)
3. [x] Draw a hand
4. [x] Real-time clock — hour, minute, thin second hand, ticking live
5. [x] Split into modules: clock.py (drawing), app.py (glue)
6. [x] timer.py — Pomodoro interval logic (focus/break lengths, phases),
       with tests (tests/test_timer.py, 6 passing)
7. [x] Soft colored arc around the rim that shrinks as the interval runs down
8. [ ] Interval preset buttons (e.g. 25/5, 120/20) + start/pause/reset
9. [x] Focus → break → focus loop (timer switches phases automatically)
10. [ ] Calming music during breaks (needs an audio library)
11. [ ] Migraine-friendly polish (minute ticks done; more as it comes)
## Decided

- GUI toolkit: tkinter (built-in; Canvas is good for drawing an analog clock)
- Look: a real-time analog clock, cartoonish-Cartier, Roman numerals in a
  soft rounded font (auto-picked from installed fonts, Baskerville-ish feel)
- Three hands showing actual current time (hour + minute + thin second)
- Pomodoro interval shown separately as a soft arc around the rim that
  shrinks as time runs out (so the clock hands stay free to tell real time)
- File structure: clock.py (drawing), timer.py (logic, coming), app.py (glue)
- Sound: none yet; calming music planned for breaks, later
- Arc sweeps counterclockwise (unwinding backward), chosen deliberately:
  feels calmer / less "hurry up" than a clockwise depleting countdown
- Arc has a small gap at the top so it reads as a gauge with a clear
  start/end, not an ambiguous full ring
- Focus arc = sage (#89a99a), break arc = muted sage-olive (#8C9579):
  distinct enough to tell phases apart at a glance, but kept in one calm
  palette so the break reads as restful, not alarming
- Minute tick marks around the rim (longer on the hours) for a classic feel
- A "face" experiment (eyes/smile) was tried and removed — too simplistic
  in tkinter to reach the intended Disney/Cogsworth warmth
## Environment note

tkinter needs Python built with Tk support. On pyenv/macOS this often
isn't the case by default — if `python -m tkinter` fails with
"No module named '_tkinter'", install Tk and rebuild Python:
    brew install tcl-tk
    pyenv install -f <version>   # with tcl-tk env vars set (see README)
then recreate the virtual environment.