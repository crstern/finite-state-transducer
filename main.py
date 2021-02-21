from fst import *
import re


def read_input(path="input.txt"):
    with open(path) as f:
        data = f.read()
    return data


if __name__ == "__main__":
    fst = FST()
    fst.read_data()
    words = re.split('[ ]+', read_input())
    for word in words:
        for char in word:
            fst.move(char)
        fst.status()
        fst.reset()
