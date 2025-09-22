# Main Launcher Script
import os

modules = {
    "Calculator": "calculator.py",
    "Study Timer": "timer.py",
    "Cyber Decoder": "decoder.py"
}

print("Operator Modules:")
for i, mod in enumerate(modules, 1):
    print(f"{i}. {mod}")

choice = int(input("Launch module #: "))
os.system(f"python {list(modules.values())[choice - 1]}")
