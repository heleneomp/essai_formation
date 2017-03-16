#!/usr/bin/env  python2

def greetings():
    """Salut RESIF people,"""
    print ("Hello RESIF peoples!")

def repeat(x, callback):
    """Call x times callback"""
    for _ in range(x):
	callback()

if __name__ == "__main__":
    repeat(3, greetings)
