#!/usr/bin/python3
def uppercase(str):
    for i in str:
        letter = i
        if 97 <= ord(i) <= 123:
            letter = chr(ord(letter) - 32)

        print(letter, end="")

    print("")
