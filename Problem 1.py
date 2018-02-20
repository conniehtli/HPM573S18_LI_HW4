from enum import Enum
import numpy as np


class Coin(Enum):
    "Heads or Tails"
    HEAD = 1
    TAIL = 0


class Game(object):
    def __init__(self, id):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(self._id)

        self._result = Coin.HEAD
        self._flipNumber = 1
        self._flipTotal = 20
        self._tailCount = 0
        self._winCount = 0

    def next_flip(self):
        if self._result == Coin.HEAD:

           if self._rnd.sample() < 0.5:
                self._result = Coin.HEAD
                self._tailCount = 0

           if self._rnd.sample() > 0.5:
                self._result = Coin.TAIL
                self._tailCount = 1

        elif self._result == Coin.TAIL:

           if self._rnd.sample() > 0.5:
                self._result = Coin.TAIL
                self._tailCount += 1

           if self._rnd.sample() < 0.5:
                if self._tailCount >= 2:
                   self._winCount += 1
                   self._result = Coin.HEAD
                   self._tailCount = 0

        self._flipNumber += 1

    def play(self):
        for i in range(1, self._flipTotal + 1):
            self._rnd = np.random
            self._rnd.seed(self._id * self._flipNumber)

            self.next_flip()

    def reward(self):
        self.play()
        self._payout = -250 + (100 * self._winCount)

        return self._payout

class Cohort:
    def __init__(self, id, game_number):
        self._listPlayers = []

        n = 1
        while n <= game_number:
            player = Game(id = id * game_number + n)
            self._listPlayers.append(player)
            n += 1

    def simulate(self):
        gameRewards = []

        for player in self._listPlayers:
            gameRewards.append(player.reward())

        cohort_average = sum(gameRewards)/len(gameRewards)
        return cohort_average

Model = Cohort(1, 1000)

print(Model.simulate())




