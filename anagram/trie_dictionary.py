from pprint import pprint
import pdb

root = {}

class Node:
    def __init__(self):
        self.children = {}
        self.words = []

class SortedTrie:
    def __init__(self):
        self.children = {}

    def add_word(self, word):
        chars = sorted(word)
        node = self
        while len(chars):
            node = node.children.setdefault(chars.pop(), Node())
        node.words.append(word)

    def find_anagram(self, word):
        chars = sorted(word)
        node = self
        while len(chars):
            char = chars.pop()
            node = node.children.get(char, None)
            if not node:
                return None
        return node.words

def load_dictionary(file_name):
    root = SortedTrie()
    with open(file_name) as file_handle:
        for word in lazy_load_dictionary(file_handle):
            root.add_word(word)
    return root

def lazy_load_dictionary(file_handle):
    for row in file_handle:
        yield row.strip().lower()

def add_word(word):
    anagram_dictionary = root
    for char in word:
        anagram_dictionary = anagram_dictionary.setdefault(char, {})
    anagram_dictionary[None] = None