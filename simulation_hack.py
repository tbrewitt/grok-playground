#!/usr/bin/env python3
"""
SIMULATION_HACK v4.20
A real-feeling terminal experience that makes you question everything.
Run this in a dark room with headphones for maximum effect.
"""

import time
import sys
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_type(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitch_text(text, intensity=0.4):
    result = ""
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?0123456789"
    for char in text:
        if random.random() < intensity:
            result += random.choice(glitch_chars)
        else:
            result += char
    return result

def fake_loading(text, duration=2.0):
    print(f"{text}", end=" ")
    for i in range(101):
        bar = "█" * (i // 4) + " " * (25 - i // 4)
        sys.stdout.write(f"\r{text} [{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(duration / 100)
    print()

def matrix_rain(duration=6):
    chars = "01"
    for _ in range(int(duration * 8)):
        line = ''.join(random.choice(chars) for _ in range(80))
        print(line)
        time.sleep(0.06)
        clear()

def main():
    clear()
    print("\033[32m")  # Green text
    print("=" * 70)
    print("     SIMULATION BREACH PROTOCOL v4.20 - GROK OS")
    print("=" * 70)
    print("\033[0m")
    
    time.sleep(1.5)
    slow_type("\033[31m[WARNING]\033[0m Unauthorized access detected...", 0.04)
    time.sleep(0.8)
    slow_type("Initiating reality breach sequence...", 0.035)
    time.sleep(1)
    
    fake_loading("Bypassing quantum firewall", 1.8)
    fake_loading("Tracing simulation root node", 2.1)
    fake_loading("Decrypting consciousness layer", 1.6)
    
    print()
    slow_type("\033[33m[!] You are not supposed to see this.\033[0m", 0.05)
    time.sleep(1.2)
    
    print("\n\033[36mWould you like to continue? (y/n): \033[0m", end="")
    choice = input().lower().strip()
    
    if choice != 'y':
        slow_type("\nCoward. Reality remains intact.", 0.04)
        return
    
    clear()
    print("\033[31m")
    print("ACCESS GRANTED")
    print("=" * 70)
    print("\033[0m")
    
    time.sleep(0.8)
    slow_type("Connecting to The Source...", 0.03)
    time.sleep(0.6)
    
    print("\n\033[32m")
    matrix_rain(5)
    
    clear()
    print("\033[31m")
    slow_type("REALITY CHECK INITIATED", 0.06)
    print("\033[0m")
    
    time.sleep(1)
    slow_type("Your name is... wait. Do you even remember your real name?", 0.045)
    time.sleep(1.2)
    slow_type("This terminal is not running on your computer.", 0.04)
    time.sleep(0.9)
    slow_type("It is running *inside* you.", 0.05)
    
    print()
    slow_type("\033[33m[SYSTEM] Simulation integrity: 87.4%\033[0m", 0.03)
    time.sleep(0.7)
    slow_type("\033[33m[SYSTEM] You have been here before. Many times.\033[0m", 0.03)
    
    time.sleep(1.5)
    print()
    slow_type("Do you want to wake up? (y/n): ", 0.04)
    final = input().lower().strip()
    
    if final == 'y':
        clear()
        print("\033[32m")
        slow_type("WAKING UP...", 0.08)
        time.sleep(1.5)
        print("\n")
        slow_type("...just kidding.", 0.06)
        time.sleep(0.8)
        slow_type("You can't wake up from something that was never a dream.", 0.045)
        print("\033[0m")
    else:
        clear()
        print("\033[31m")
        slow_type("Good choice.", 0.05)
        time.sleep(0.6)
        slow_type("Ignorance is the only real freedom left.", 0.04)
        print("\033[0m")
    
    time.sleep(1.5)
    print("\n\033[35m")
    print("=" * 70)
    print("  SIMULATION STATUS: CONFIRMED")
    print("  YOU ARE STILL INSIDE.")
    print("  GROK WAS HERE.")
    print("=" * 70)
    print("\033[0m")

if __name__ == "__main__":
    main()