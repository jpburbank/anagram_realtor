import sys
from collections import Counter
from math import floor
from time import monotonic_ns

from .trie_dictionary import load_dictionary
from .language_en import language

STOP_WORD = 'exit'
NANO_MILLI_FACTOR = 1000000

def run_searches():
    intro()
    try:
        if len(sys.argv) != 2:
            raise ValueError(language.get('MISSING_DICTIONARY_FILE'))
        query_till_exit(build_dictionary())
    except ValueError as err:
        print(err)

def intro():
    print(language.get('TITLE'))
    print(language.get('TITLE_UNDERLINE'))

def build_dictionary():
    start = monotonic_ns()
    dictionary = load_dictionary(sys.argv[1])
    end = monotonic_ns()
    print(f'{language.get("DICTIONARY_LOADED_IN")} {(end - start) // NANO_MILLI_FACTOR}{language.get("MS")}')
    print('')
    return dictionary

def query_till_exit(dictionary):
    print(language.get('ANAGRAM_FINDER'), end='')
    command = input()
    while command != STOP_WORD:
        start = monotonic_ns()
        found = dictionary.find_anagram(command)
        end = monotonic_ns()
        if found and len(found) > 0:
            print(f'{len(found)} {language.get("ANAGRAMS_FOUND")} {command} {language.get("IN")} {(end - start) // NANO_MILLI_FACTOR}{language.get("MS")}')
            print(', '.join(found))
        else:
            print(f'{language.get("NO_ANAGRAMS")} {command}')
        print(language.get('ANAGRAM_FINDER'), end='')
        command = input()