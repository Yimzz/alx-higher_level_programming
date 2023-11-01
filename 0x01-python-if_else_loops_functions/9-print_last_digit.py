#!/usr/bin/python3
def print_lat_digit(number):
    number = abs(number) % 10
    print(number, end="")
    return number
