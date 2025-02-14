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

    def random_choice(self):
        return random.choice(self.word_list)
