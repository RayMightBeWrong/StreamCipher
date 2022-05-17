#!/usr/bin/python3

import sys


def encrypt(key, chars):
    res = []
    curKey = 0
    for char in chars:
        res.append(encryptChar(key[curKey], char))
        curKey = (curKey + 1) % len(key)
    return res

def encryptChar(keyValue, char):
    bKey = ord(keyValue)
    bChar = ord(char)
    xor = bin(bKey ^ bChar)
    return chr(int(xor, 2))


if len(sys.argv) == 4:
    key = list(input("Key to encrypt file with: "))

    rfile = open(sys.argv[1], "r")

    if sys.argv[2] == '-w':
        wfile = open(sys.argv[3], "w")
    if sys.argv[2] == '-a':
        wfile = open(sys.argv[3], "a")

    chars = list(rfile.read())
    res = encrypt(key, chars)
    wfile.write("".join(res))

    wfile.close()
    rfile.close()
