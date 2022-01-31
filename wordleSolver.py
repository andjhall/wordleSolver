#!/usr/bin/python3

import sys
from functools import cmp_to_key
from collections import Counter


letter_freqs = {
    "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
    "G": .02015, "H": .06094, "I": .06996, "J": .00153, "K": .00772, "L": .04025,
    "M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
    "S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
    "Y": .01974, "Z": .00074
}


def is_unique(word):
    # Initialize occurrences of all characters
    char_set = [False] * 128
 
    # For every character, check if it exists
    # in char_set
    for i in range(0, len(word)):
 
        # Find ASCII value and check if it
        # exists in set.
        val = ord(word[i])
        if char_set[val]:
            return False
 
        char_set[val] = True
 
    return True

def print_options():
    print("Enter the number corresponding to the result of each letter")
    print("1: Right letter, right spot")
    print("2: Right letter, wrong spot")
    print("3: Wrong letter")


def get_unique_list(words):
    u_items = []
    for item in words:
        if (is_unique(item[0])):
                u_items.append(item)
    return u_items


if __name__ == "__main__":
    print("Wordle.py")

    # create word/weight lists
    word_weights = []
    unique_words = []

    # read in words file
    with open("wordList.txt", 'r') as file:
        lines = file.readlines()

        for line in lines:

            # convert words to upper case
            line = line.upper()
            word = ""
            sum = 0
            for i in range(0,5):
                sum += letter_freqs[line[i]]
                word += line[i]

            item = [word, sum]
            word_weights.append(item)

            # Copy words with no duplicate letters to a second list
            if (is_unique(word)):
                unique_words.append(item)
    

    word_weights.sort()
    unique_words.sort(key = lambda x: x[1], reverse=True)

    # Final answer
    ans = ["_","_","_","_","_"]

    print("Try one of these words first:")
    print(unique_words[0][0])

    # The first 3 unique words are just combinations of the same 5 characters
    for i in range(3,8):
        print(unique_words[i][0])

    while ('_' in ans):
        # Get user input
        usr_input = ""

        # Ensure user input is exactly 5 characters
        while (len(usr_input) != 5):
            print()
            usr_input = input("Enter your guess: ")
            usr_input = usr_input.upper()
            if (len(usr_input) != 5):
                print("Please enter a 5 letter word")

        # Get feedback on each character
        print_options()
        for i in range(0,5):
            ltr = usr_input[i]
            res = input("Input result for letter " + ltr + ": ")
            print()

            # 3 options
            # Option 1: Right letter, right location
            # Remove all words that don't have this letter in this location
            if (int(res) == 1):
                ans[i] = ltr
                tmp_words = []
                for item in word_weights:
                    if (item[0][i] == ltr):
                        tmp_words.append(item)
                word_weights.clear()
                word_weights = tmp_words.copy()
            
            # Option 2: Right letter, wrong location
            # Remove all words that don't have this letter, or have this letter in the chosen location
            elif (int(res) == 2):
                tmp_words = []
                for item in word_weights:
                    if (ltr in item[0]):
                        if (item[0][i] != ltr):
                            tmp_words.append(item)
                word_weights.clear()
                word_weights = tmp_words.copy()
            
            # Option 3: Wrong letter
            # Remove all words that contain this letter
            else:
                tmp_words = []
                for item in word_weights:
                    if (ltr not in item[0]):
                        tmp_words.append(item)
                word_weights.clear()
                word_weights = tmp_words.copy()

        print()
        unique_words.clear()
        unique_words = get_unique_list(word_weights)
        unique_words.sort(key = lambda x: x[1], reverse=True)
        word_weights.sort(key = lambda x: x[1], reverse=True)


        print("Current answer: " + "".join(ans))
        print()

        print("Try these words next: ")
        full_list_length = len(word_weights)
        subset_length = len(unique_words)
        
        # Get new suggestions
        if (subset_length >= 5):
            for i in range(0,5):
                text = "word: " + unique_words[i][0]
                text += "\tweight: {:.4f}".format(unique_words[i][1])
                print(text)
        
        elif (subset_length < 5 and full_list_length > 5 - subset_length):
            for i in range(0, subset_length):
                text = "word: " + unique_words[i][0]
                text += "\tweight: {:.4f}".format(unique_words[i][1])
                print(text)
            for i in range(0, 5 - subset_length):
                text = "word: "+ word_weights[i][0]
                text += "\tweight: {:.4f}".format(word_weights[i][1])
                print(text)
    
        elif (subset_length <= 0 and full_list_length >= 5):
            for i in range(0,5):
                text = "word: "+ word_weights[i][0]
                text += "\tweight: {:.4f}".format(word_weights[i][1])
                print(text)

        elif (full_list_length < 5 and full_list_length > 0):
            for i in range(0, full_list_length):
                text = "word: "+ word_weights[i][0]
                text += "\tweight: {:.4f}".format(word_weights[i][1])
                print(text)
        
        print("Number of words in subset: " + str(subset_length))
        print("Number of words in full word list: " + str(full_list_length))

        print()
