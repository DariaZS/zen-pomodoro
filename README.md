# Zen Pomodoro

A calm, migraine-friendly Pomodoro timer built around a real-time analog
clock. Cartier-ish look, soft muted colors, gentle motion — a clock you'd
be happy to just have on screen, that also times your focus sessions.

## What it does

- A real-time analog clock (hour, minute, thin second hand) in a soft
  charcoal palette with Roman numerals
- (Coming) A soft arc around the rim that shrinks as a focus interval runs
  down, with preset lengths and a focus → break loop
- (Later) Calming music during breaks

## Structure

- `clock.py` — all the drawing (face, numerals, hands, arc)
- `timer.py` — Pomodoro interval logic *(coming)*
- `app.py` — the app you run; builds the window and wires it together

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # .venv\Scripts\activate on Windows
```

No pip packages yet — v1 uses only tkinter, which ships with Python.

**Note:** tkinter needs Python built with Tk support. On pyenv/macOS this
often isn't the default. If `python -m tkinter` fails with "No module named
'_tkinter'":

```bash
brew install tcl-tk
env \
  PATH="$(brew --prefix tcl-tk)/bin:$PATH" \
  LDFLAGS="-L$(brew --prefix tcl-tk)/lib" \
  CPPFLAGS="-I$(brew --prefix tcl-tk)/include" \
  PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig" \
  pyenv install -f <your-python-version>
```

Then recreate your virtual environment.

## Run

```bash
python app.py
```

## Status

🚧 Early build. Real-time clock working; Pomodoro interval arc, presets,
and the focus/break loop are next.