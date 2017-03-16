#!/usr/bin/env  python2

def greetings():
print "Hello RESIF people!"

def repeat(x, callback):
    for _in range(x):
	callback()

if __name__ == "__main__":
    greetings()

