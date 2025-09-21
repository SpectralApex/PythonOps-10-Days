# alarm_clock.py
# Simple text alarm (beeps on Windows, prints elsewhere)
import time
import datetime
import sys
import platform

def beep():
    if platform.system() == "Windows":
        try:
            import winsound
            winsound.Beep(1000, 800)
            return
        except Exception:
            pass
    # Fallback: terminal bell (may not work everywhere)
    sys.stdout.write("\a")
    sys.stdout.flush()

def main():
    print("Alarm Clock")
    print("Enter time in 24h format HH:MM or HH:MM:SS")
    alarm_str = input("Alarm time: ").strip()
    try:
        fmt = "%H:%M:%S" if len(alarm_str.split(":")) == 3 else "%H:%M"
        target = datetime.datetime.combine(
            datetime.date.today(),
            datetime.datetime.strptime(alarm_str, fmt).time()
        )
        if target <= datetime.datetime.now():
            target += datetime.timedelta(days=1)
    except ValueError:
        print("Invalid time format.")
        return

    print(f"Alarm set for {target.strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        while True:
            now = datetime.datetime.now()
            remaining = (target - now).total_seconds()
            if remaining <= 0:
                print("\nWake up! Alarm time reached.")
                for _ in range(5):
                    beep()
                    time.sleep(0.5)
                break
            # Update every second
            sys.stdout.write(f"\rTime now: {now.strftime('%H:%M:%S')} | Remaining: {int(remaining)}s ")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAlarm cancelled.")

if __name__ == "__main__":
    main()
