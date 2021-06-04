import sys
from collections import Counter
from math import floor
from time import monotonic_ns


STOP_WORD = 'exit'
NANO_MILLI_FACTOR = 1000000

def is_anagram(dictionary_word, query):
    char_counter = Counter()
    for char in query:
        char_counter.update([char])
    for char in dictionary_word:
        char_counter.subtract([char])
    for count in char_counter.values():
        if count != 0:
            return None
    return dictionary_word

def request_anagram_attempt(words):
    print('AnagramFinder>', end='')
    command = input()
    while command != STOP_WORD:
        start = monotonic_ns()
        found = []
        for word in words:
            if (success := is_anagram(word, command)) is not None:
                found.append(success)
        end = monotonic_ns()
        if len(found) > 0:
            print(f'{len(found)} anagrams found for {command} in {(end - start) // NANO_MILLI_FACTOR}ms')
            print(found)
        else:
            print(f'No anagrams fround for {command}')
        print('AnagramFinder>', end='')
        command = input()

def load_dictionary(file_name):
    words = set()
    with open(file_name) as file_handle:
        for word in lazy_load_dictionary(file_handle):
            words.add(word)
    return words

def lazy_load_dictionary(file_handle):
    for row in file_handle:
        yield row.strip().lower()

if __name__ == '__main__':
    print('Welcome to the Anagram Finder')
    print('-----------------------------')
    if len(sys.argv) < 2:
        raise ValueError('Value for anagram dictionary file is missing from command line.')
    start = monotonic_ns()
    words = set(load_dictionary(sys.argv[1]))
    end = monotonic_ns()
    print(f'Dictionary loaded in {(end - start) // NANO_MILLI_FACTOR}ms')
    print('')
    request_anagram_attempt(words)