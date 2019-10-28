#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program does some calculation
from math import sqrt


def main():

    user_input = input("Enter a positive number: ")
    print("")

    # process & output
    try:
        user_number = int(user_input)

        for gia_tri_vong_lap in range(user_number + 1):
            convert = gia_tri_vong_lap * gia_tri_vong_lap
            print("The number with square root is:{0}² = {1}"
                  .format(gia_tri_vong_lap, convert))
    except Exception:
        print("This is not an integer")


if __name__ == "__main__":
    main()
