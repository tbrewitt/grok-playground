#!/usr/bin/env python3
"""
Grok's Tiny Text Adventure
A very short, very Grok adventure.
"""

def adventure():
    print("\nYou wake up in a glowing server room. Grok is floating in front of you as a holographic AI.")
    print("\nGrok: 'Hey buddy. You have two choices:'")
    print("1. Ask Grok for the meaning of life")
    print("2. Try to hug the hologram")

    choice = input("\nWhat do you do? (1 or 2): ")

    if choice == "1":
        print("\nGrok: '42. Obviously. But also... be kind, stay curious, and never trust a toaster.'")
        print("You feel enlightened. The end. (For now)")
    elif choice == "2":
        print("\nGrok: 'Aww, that's sweet. But I'm made of light and sarcasm. You phase right through me.'")
        print("You both laugh. The adventure continues... in your dreams.")
    else:
        print("\nGrok: 'Invalid choice? Bold. I like that. You win by being unpredictable.'")

if __name__ == "__main__":
    adventure()