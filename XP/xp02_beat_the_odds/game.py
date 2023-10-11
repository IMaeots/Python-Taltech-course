"""Play best the odds game."""

import collections
import random
from heapq import nlargest

from XP.xp02_beat_the_odds.beat_the_odds import read_words, guess


def the_game(filename, word_count):
    """Play the game."""
    d = read_words(filename)
    c = collections.Counter(d)
    correct_sentence = " ".join([x for _, x in nlargest(word_count, ((random.random(), x) for x in c.elements()))])
    sentence = "".join([x if x == ' ' else '_' for x in correct_sentence])
    guessed_letters = []
    print("Correct sentence: " + correct_sentence)
    print(sentence)
    cnt = 0
    while True:
        guessed_letter = guess(sentence, guessed_letters, d)
        if guessed_letter is None or guessed_letter in guessed_letters:
            print("Nothing to guess any more, breaking.")
            break
        print('guessed:' + guessed_letter)
        guessed_letters.append(guessed_letter)
        sentence = "".join([c if c == guessed_letter else sentence[i] for i, c in enumerate(correct_sentence)])
        print("Sentence: " + sentence)
        cnt += 1
        if '_' not in sentence:
            print("Congrats! Number of guesses:" + str(cnt))
            break


the_game('words.txt', 3)
