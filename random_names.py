#!/usr/bin/env python3

import random

SEX = 'boy'
NAME_WORD_COUNT = 2

def get_all_words():
    with open('words_' + SEX + '.txt', encoding='utf-8') as f:
        return list(map(lambda s: s.strip(), f.readlines()))

def random_name():
    words = random.choices(get_all_words(), k=NAME_WORD_COUNT)
    return ''.join(words)

if __name__ == '__main__':
    for i in range(10):
        print(i, random_name())

