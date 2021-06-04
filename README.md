# Anagram Finder Programming Task

## Summary
This application is an assignment given to myself as part of the hiring process at realtor.com. This version is the second of two asked for. It represents a refined version, as asked for by the given instructions. The approach uses a trie data structure for a faster lookup time. 

## Trie data structure
The trie used is a variation on a traditional word completion trie. The change is that the nodes in the trie are in alphabetical ascending single character order as the nodes move down from the root. When each word goes into the trie during dictionary creation, its unsorted string is copied into a set collection once it expends the sorted chars as nodes. This allows a single transveral of nodes to get all of the anagrams per word. For example the dictionary words 'yah' and 'hay' would share a node path of a->h->y and have the 'y' node would contain the words ['yah' and 'hay']. So a single pass of the query word 'ahy' would get both anagrams.

## Requirements
This was written in Python version 3.9.4. Python version 3.8.0 and higher should also work. No third part libraries where used. It is required that the dictionary file be in the project root. The project will be tarred and gzipped with the dictionary file there. A note on the language. I chose Python because I find it a good quick tool for prototyping and interview questions. As a language for this type of application in production, it would be a poor choice for performance reasons. A compiled language would be better.

## Assumptions
I have made the assumption that a letter is a letter, regardless if it is upper or lower case. Meaning the word "Bob" is equivalent to the word "bob". 

## Running
The application will run by the following command

<pre><code>python3 main.py dictionary.txt</code></pre>
Your environment may not need use the command "python3", but just "python"

## Complexity
Search complexity is O(N) where N is the number of characters in a queried words.

## Concerns
The major concern with this algorithm is that it requires the whole datastructure to be held in memory, if its to maintain its speed. This could be a concern with very large sized dictionaries.

## Polish
I wanted to simulate a production application. I added an adhoc language locatization. Its on the naive side, but its a requirement to not use any third party libraries. I would also have liked to have the time add unit tests and PnR tests to it as well.

## Source control
This assignment can be found as a public repo on Github, with the URL https://github.com/jpburbank/anagram_realtor. This version is the branch second_version. The .git files have been removed from the tarred submission.