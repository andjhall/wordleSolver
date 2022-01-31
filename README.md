wordleSolver
=========

A simple tool to assist users in solving the daily Wordle puzzle

Created by Andrew Hall <andjhall@umich.edu>

## Quick start
```console
$ git clone
$ cd wordleSolver
$ python3 wordleSolver.py
```

## About
This program was created to provide suggestions to help users solve Wordle puzzles. A list of 5 letter English words from Stanford is used as the subset of possible solutions to the puzzle, and this list can be found at [https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt](https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt).

Each word is given a score which is calculated by taking the sum of each letter's frequency. For more information, see the [Wikipedia Page](https://en.wikipedia.org/wiki/Letter_frequency) on Letter Frequency. The 5 words with the highest scores will be suggested to the user.

## Contributing
Contributions are welcome! Please feel free to make edits on a branch and create a merge request into main. For any questions, please reach out to me at <andjhall@umich.edu>.