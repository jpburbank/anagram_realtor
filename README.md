# Anagram Finder Programming Task

## Summary
This application is an assignment given to myself as part of the hiring process at realtor.com. This version is the first of two asked for. It represents the "quick and dirty" version, as asked for by the given instructions.

## Requirements
This was written in Python version 3.9.4. Python version 3.8.0 and higher should also work. No third part libraries where used. It is required that the dictionary file be in the project root. The project will be tarred and gzipped with the dictionary file there.

## Assumptions
I have made the assumption that a letter is a letter, regardless if it is upper or lower case. Meaning the word "Bob" is equivalent to the word "bob". 

## Running
The application will run by the following command

<pre><code>python3 main.py dictionary.txt</code></pre>
Your environment may not need use the command "python3", but just "python"

## Complexity
I used this type of solution for the first attempt as the instructions say to do a "quick and dirty" approach first. Consequently the time complexity for finding anagrams in this solution is O(N*M). Where N is the amount of words in the dictionary and M is the maximum character length a word in the dictionary or the user provided word.