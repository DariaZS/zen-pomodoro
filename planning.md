# Planning — Zen Pomodoro

A calm, migraine-friendly Pomodoro timer. An old-school analog clock face,
soft muted colors, gentle visuals — no harsh flashing, no jarring alarms.
Runs as its own desktop window.

## Goals

- Analog clock face with a hand that sweeps as the interval counts down
- Migraine-friendly design: soft charcoal palette, low contrast, calm
- Preset intervals (Focus 25, breaks, etc.) the user can pick
- Runs locally as a desktop app first; distribution decided later

## Tech choices

- **Python + tkinter** for the GUI. tkinter is built into Python (no
  install), and its Canvas widget is ideal for *drawing* an analog clock
  (circles, tick marks, rotating hands).
- No sound in v1 — calming music/chimes planned for a later version
  (will need an audio library like pygame at that point).

## Build order (small steps, each runnable)

1. [ ] Empty window appears
2. [ ] Draw a static clock face (rim, face, tick marks)
3. [ ] Draw a hand pointing at a given position
4. [ ] Count down — hand sweeps, digital readout updates
5. [ ] Preset interval buttons + start/pause/reset controls
6. [ ] Migraine-friendly polish (gentle transitions, dimming)

## Decided

- GUI toolkit: tkinter (built-in, Canvas good for analog clock)
- Look: analog clock face with hands
- Sound: none in v1, add later

## Later / maybe

- Calming looping music or gentle start/end chimes
- Packaging into a double-clickable Mac .app (PyInstaller)
- App Store distribution — noted as hard with Python; revisit only if
  the app becomes something worth shipping