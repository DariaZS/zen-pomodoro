"""
Tests for timer.py — pure logic, no GUI needed.

Run from the project root with:  python -m pytest tests/ -v
"""

import os
import sys

# let the test find timer.py in the parent folder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from timer import PomodoroTimer


def test_starts_in_focus_phase():
    t = PomodoroTimer(focus_minutes=25, break_minutes=5)
    assert t.phase == "focus"
    assert t.remaining == 25 * 60


def test_does_not_tick_when_paused():
    t = PomodoroTimer()
    # not started, so tick should do nothing
    t.tick()
    assert t.remaining == 25 * 60


def test_counts_down_one_second_per_tick():
    t = PomodoroTimer()
    t.start()
    t.tick()
    assert t.remaining == 25 * 60 - 1


def test_fraction_remaining():
    t = PomodoroTimer(focus_minutes=10)
    t.start()
    # full at the start
    assert t.fraction_remaining() == 1.0


def test_switches_from_focus_to_break():
    # tiny timer so we can run it to zero quickly
    t = PomodoroTimer(focus_minutes=0, break_minutes=5)
    t.start()
    # focus has 0 seconds, so the next tick should switch to break
    switched = t.tick()
    assert switched is True
    assert t.phase == "break"
    assert t.remaining == 5 * 60


def test_switches_break_back_to_focus():
    t = PomodoroTimer(focus_minutes=0, break_minutes=0)
    t.start()
    t.tick()               # focus -> break
    assert t.phase == "break"
    switched = t.tick()    # break -> focus
    assert switched is True
    assert t.phase == "focus"