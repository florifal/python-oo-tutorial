import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):

    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return 0


class MostVowels(WordGame):
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        words = [player1_word, player2_word]
        vowel_count = [0, 0]

        for player, word in enumerate(words):
            for c in word:
                if c.lower() in MostVowels.vowels:
                    vowel_count[player] += 1

        return vowel_count.index(max(vowel_count)) + (vowel_count.count(max(vowel_count)) == 1)


class RockPaperScissors(WordGame):
    objects = ['rock', 'paper', 'scissors']

    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        player1_word = player1_word.lower()
        player2_word = player2_word.lower()

        if player1_word not in RockPaperScissors.objects and player2_word in RockPaperScissors.objects:
            return 2
        elif player1_word in RockPaperScissors.objects and player2_word not in RockPaperScissors.objects:
            return 1
        elif player1_word not in RockPaperScissors.objects and player2_word not in RockPaperScissors.objects:
            return 0
        else:
            p1_i = RockPaperScissors.objects.index(player1_word)
            p2_i = RockPaperScissors.objects.index(player2_word)
            return (p1_i - p2_i) % 3


if __name__ == "__main__":
    # p = WordGame(3)
    # p.play()

    # p = LongestWord(3)
    # p.play()

    # p = MostVowels(3)
    # p.play()

    p = RockPaperScissors(3)
    p.play()
