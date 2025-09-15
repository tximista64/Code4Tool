#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

tirade = """
""".strip("\n")

code = [37, 14, 6, 16, 13, 247, 4, 3, 5, 11, 7, 14, 6, 5, 21, 1, 249] #wtf?!

def main():
    text = tirade
    text = text.replace(" ", "").replace("\n", "")
    out_chars = []
    for n in code:
        out_chars.append(text[n-1])
    result = "".join(out_chars)
    print(result)

if __name__ == "__main__":
    main()

