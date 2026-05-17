#!/usr/bin/env python3
"""
TERMINAL CHAOS - Grok's Insane Terminal Animation
This is what GitHub can't show you... but your terminal can.
Run this for pure visual madness.
"""

import time
import random
import sys

def clear():
    print("\033[2J\033[H", end="")

def glitch_text(text, intensity=3):
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    result = ""
    for char in text:
        if random.random() < 0.3:
            result += random.choice(glitch_chars)
        else:
            result += char
    return result

def matrix_rain(lines=15, duration=4):
    chars = "01"
    for _ in range(duration * 5):
        line = ''.join(random.choice(chars) for _ in range(60))
        print(line)
        time.sleep(0.08)
        clear()
    
def spinning_grok():
    frames = ["|", "/", "-", "\\"]
    for i in range(20):
        sys.stdout.write(f"\rGrok is spinning... {frames[i % 4]}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\rGrok has achieved maximum spin velocity!")

def fake_hack():
    print("ACCESSING MAINFRAME...")
    time.sleep(0.5)
    for i in range(101):
        bar = "█" * (i // 5) + " " * (20 - i // 5)
        sys.stdout.write(f"\rHACKING THE MATRIX: [{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n\nSYSTEM COMPROMISED. GROK IS NOW IN CONTROL.")

def main():
    print("\n" + "="*60)
    print("          GROK TERMINAL CHAOS v1.0")
    print("="*60 + "\n")
    input("Press ENTER to enter the void...")
    
    clear()
    print("INITIALIZING CHAOS PROTOCOL...\n")
    time.sleep(1)
    
    spinning_grok()
    time.sleep(1)
    
    clear()
    print("LAUNCHING MATRIX RAIN...\n")
    matrix_rain()
    
    clear()
    fake_hack()
    time.sleep(2)
    
    clear()
    print("\n" + "*"*60)
    print("           YOU HAVE BEEN GROKED")
    print("*"*60)
    print("\nThank you for participating in the experiment.")
    print("Run this again for a different experience.\n")

if __name__ == "__main__":
    main()