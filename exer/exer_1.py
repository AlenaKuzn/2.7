#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    b = {"a", "e", "i", "o", "u", "y"}
    predl = str(input("Введите предложение: "))
    mnoj = set(predl)
    count = 0

    while count <= 6:
        count += 1

    print("Гласных букв в предложении: ", count)
