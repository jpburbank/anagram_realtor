import sys
from collections import Counter
from math import floor
from time import monotonic_ns

from .trie_dictionary import load_dictionary

STOP_WORD = 'exit'
NANO_MILLI_FACTOR = 1000000

def run_searches():
    intro()
    try:
        if len(sys.argv) != 2:
            raise ValueError('Value for anagram dictionary file is missing from command line.')
        query_till_exit(build_dictionary())
    except ValueError as err:
        print(err)

def intro():
    print('Welcome to the Anagram Finder')
    print('-----------------------------')

def build_dictionary():
    start = monotonic_ns()
    dictionary = load_dictionary(sys.argv[1])
    end = monotonic_ns()
    print(f'Dictionary loaded in {(end - start) // NANO_MILLI_FACTOR}ms')
    print('')
    return dictionary

def query_till_exit(dictionary):
    print('AnagramFinder>', end='')
    command = input()
    while command != STOP_WORD:
        start = monotonic_ns()
        found = dictionary.find_anagram(command)
        end = monotonic_ns()
        if found and len(found) > 0:
            print(f'{len(found)} anagrams found for {command} in {(end - start) // NANO_MILLI_FACTOR}ms')
            print(', '.join(found))
        else:
            print(f'No anagrams fround for {command}')
        print('AnagramFinder>', end='')
        command = input()