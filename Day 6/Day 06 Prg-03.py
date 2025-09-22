# Focus Timer
import time

def focus_timer(minutes):
    print(f"Focus mode activated for {minutes} minutes.")
    time.sleep(minutes * 60)
    print(" Time's up! Take a break.")

focus_timer(2)  # Pomodoro-style
