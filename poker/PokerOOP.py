
from Card import *

class Hand():
    def __init__(self):
        self.values = []
        for c in range(5):
            card = Card()
            while card in self.values:
                card = Card()
            self.values.append(card)
        self.values.sort()
        self.score = None

    def getHighestType(self):
        if isStraight() and isFlush():
            self.score = 0
        elif hasNumMatchingCards(4):
            self.score = 1
        elif hasGroups(3, 2):
            self.score = 2
        elif isFlush():
            self.score = 3
        elif isStraight():
            self.score = 4
        elif hasNumMatchingCards(3):
            self.score = 5
        elif hasGroups(2, 2):
            self.score = 6
        elif hasNumMatchingCards(2):
            self.score = 7
        else:
            self.score = 8

    def isFlush(self):
        for i in range(5):
            if not self.values[i].isSameSuit(self.values[0]):
                return False
        return True

    def isStraight(self):
        for i in range(5):
            if self.values[i].rank != self.values[0].rank + i:
                return False
        return True

    def hasGroups(size1, size2): # size1 + size2 <= 5
        hand = self.values
        hand = removeMatchingCards(hand,size1)
        hand = removeMatchingCards(hand,size2)
        if (len(tmpHand) == 5 - size1 - size2):
            return True
        return False

    def hasNumMatchingCards(self, number):
        ranks = []
        for card in self.values:
            ranks.append(card.rank)
        for i in range(1,13):
            if ranks.count(i) == number:
                return True
        return False

    def removeMatchingCards(self, number):
        hand = []
        hand.extend(self.values)

        ranks = []
        match = 0

        for card in self.values:
            ranks.append(card.rank)
        for i in range(1,13):
            if ranks.count(i) == number:
                match = i
        if match != 0:
            for i in range(number):
                hand.remove(hand[ranks.index(match)])
        return hand

