#!/usr/bin/python3
"""
module that convers a string into
a number
"""
from word2number import w2n

def convert(text):
    """ converts str into int """
    try:
        num = int(text)
        if num < 0:
            return 0
        else:
            return num
    except ValueError:
        pass
    return text_to_num(text)

def text_to_num(text):
    """ handles the case where
        the str comes from speech-to-text"""
    keys = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty",
        "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred",
        "thousand", "million", "billion", "trillion"
      ]
    size = len(text)
    word = ""
    idx = size
    while idx > -1:
        found = False
        for i in range(idx - 1, -1, -1):
            sub_word = text[i:idx]
            if sub_word in keys:
                found = True
                word = text[i:idx] + word
                if word != "":
                    word = " " + word
                idx = i + 1
                break
        idx -= 1
        if idx == 0:
            break
        if not found:
            return 0
    try:
        return w2n.word_to_num(word)
    except ValueError:
        return 0
