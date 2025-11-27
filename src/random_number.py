#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#
import random

MAX_RAND = 100


def generate_random_number(max: int) -> int:
    return random.random() * max


if __name__ == "__main__":
    rand_num = int(generate_random_number(MAX_RAND))
    print("The random number is: ", rand_num)
