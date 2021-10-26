import time
import sys
import random

LANGUAGE = "greek"

words = []
word_num = 0

for line in open(LANGUAGE + "_words.txt"):
    if line:
        words.append(line.replace("\n", ""))


def add_batch(array):
    for w in random.choices(words, k=20):
        array.insert(0, w)
        

if __name__ == "__main__":

    challenge_words = []
    add_batch(challenge_words)

    running = True
    print("Hello, let's find out how fast you type.")
    print("Type in the words as they appear")
    game_mode = int(input("Enter 1 for infinite or 2 for challenge..."))
    print("Starting in...")
    for i in range(0, 3):
        print(3 - i)
        time.sleep(1)

    response_words = []
    failures = 0
    
    start = (int(time.time()))

    while running is True:

        if game_mode == 1:
            if len(challenge_words) <= 5:
                add_batch(challenge_words)

        line = challenge_words.pop().split("\t")
        print(line)
        word_chunk = line[0]
        word_trans = line[2]
        word_phon = line[1]
        print("\033[90m", end="")

        print(word_chunk, "->", "meaning %s, pronounced: %s" % (word_trans, word_phon))

        if len(challenge_words) > 0:
            response = input(challenge_words[-1] + "\033[A\r\033[93m")
        else:
            response = input("\033[A\r\033[93m")

        if (response == word_chunk):
            print("\033[92m", end="")
        else:
            print("\033[91m", end="") 
            failures += 1

        print("\033[A\r" + response)
        word_num += 1
        if game_mode == 1:
            if failures >= 3:
                running = False
        if game_mode == 2:
            if word_num >= 20:
                running = False

    
    end = (int(time.time()))
    diff = end-start

    print("\033[96mYour time was: %d seconds" % (diff))
    print("You typed: %d words" % word_num)
    print("With %s failures, that gives a wpm of: %d" % (failures, (word_num - failures) / diff * 60 ))

