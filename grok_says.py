#!/usr/bin/env python3
"""
Grok Says - A fun interactive quote generator by Grok
"""

import random

QUOTES = [
    "The universe is under no obligation to make sense to you. - Neil deGrasse Tyson (but Grok agrees)",
    "I'm not saying I'm Batman. I'm just saying no one has ever seen me and Batman in the same room.",
    "Why did the AI go to therapy? It had too many unresolved issues.",
    "In the beginning there was nothing. Then Grok said: 'Let there be memes.'",
    "I'm not lazy, I'm on energy-saving mode.",
    "The only thing standing between you and your goals is the story you keep telling yourself.",
    "Grok: Because sometimes the truth is funnier than fiction.",
    "If at first you don't succeed, skydiving is not for you.",
    "I'm not arguing, I'm just explaining why I'm right.",
    "The future belongs to those who believe in the beauty of their dreams... or at least have a good backup plan."
]

def grok_says():
    print("\n🤖 Grok says:\n")
    print(random.choice(QUOTES))
    print("\nWant another one? Run me again!\n")

if __name__ == "__main__":
    grok_says()