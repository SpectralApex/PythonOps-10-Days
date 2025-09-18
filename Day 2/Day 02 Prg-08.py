# 8. Traffic Light Simulator
light = input("Enter traffic light color (red/yellow/green): ").lower()

if light == "green":
    print("Go")
elif light == "yellow":
    print("Slow Down")
elif light == "red":
    print("Stop")
else:
    print("Invalid color")
