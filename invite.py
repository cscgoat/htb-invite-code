#!/usr/bin/python3

''' HackTheBox crack invite code '''

import sys
import base64
import json

def rot13(text):
    cipher = ""
    for t in text:
        tord = ord(t)
        c = tord + 13

        if tord > 64 and tord < 91:
            if c > 90: c -= 26
            cipher += chr(c)
        elif tord > 96 and tord < 123:
            if c > 122: c -= 26
            cipher += chr(c)
        else: cipher += t
    return cipher

def decode(string):
    return base64.b64decode(string).decode('latin-1')

# Not secure. For purpose of this exercise ONLY!
print(locals()[sys.argv[1]](sys.argv[2]))
