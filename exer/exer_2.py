#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    one = str(input("Введите первую строку: "))
    two = str(input("Введите вторую строку: "))
    mnoj_1 = set(one)
    mnoj_2 = set(two)

    print("Общие символы: ", mnoj_1.intersection(mnoj_2))
