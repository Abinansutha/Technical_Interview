import random


class Word:
    def __init__(self):
        word_dict = {
            "four-letter-words": [
                "able",
                "belt",
                "bolt",
                "cast",
                "cash",
                "knot",
                "note",
                "near",
                "over",
                "salt",
                "wind",
            ]
        }
        self.word_list = word_dict["four-letter-words"]
        self.target_word = self.random_choice()
        self.attempts = 1
        self.max_attempts = 5

    def random_choice(self):
        return random.choice(self.word_list)

    def guess_word(self, guess):
        if guess == self.target_word:
            return True
        else:
            return False

    def play_game(self):
        print(self.target_word)
        print(
            "Welcome to Word Guess! You have 5 turns to guess the word. Please enter your first guess: "
        )
        while self.attempts <= self.max_attempts:
            guess = input("Enter a four letter word: ")

            self.attempts += 1

            if self.guess_word(guess):
                print("You got it! Amazing! ")
                break

            elif self.attempts > self.max_attempts:
                print("Your out of turns game over")

            else:
                print("Wrong Guess Try Again! ")


word = Word()
word.play_game()
