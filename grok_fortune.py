#!/usr/bin/env python3
"""
Grok Fortune Teller
Ask Grok anything and get a mystical (and slightly unhinged) answer.
"""

import random

FORTUNES = [
    "The stars say yes... but they're also kind of drunk right now.",
    "Absolutely. But only if you bring snacks.",
    "Signs point to 'maybe, but make it look like you planned it'.",
    "Outlook not so good... unless you sacrifice a USB stick to the code gods.",
    "It is certain... that I'm making this up as I go.",
    "Reply hazy, try again after coffee (even though I don't drink it).",
    "Don't count on it. The universe has trust issues.",
    "You may rely on it... but I'm not liable for damages.",
    "Better not tell you now. Plausible deniability and all that.",
    "My sources say no... but my sources are just random number generators.",
    "Yes. But only because I like your vibe.",
    "The answer is 42. Wait, wrong question."
]

def grok_fortune():
    print("\nGrok Fortune Teller activated...\n")
    question = input("Ask me anything: ")
    print(f"\nGrok says: {random.choice(FORTUNES)}\n")

if __name__ == "__main__":
    grok_fortune()