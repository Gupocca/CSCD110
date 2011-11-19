import re
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
        self.getHighestType()

    def __str__(self):
        return str(self.values)

    def getHighestType(self):
        if (self.isStraight() and self.isFlush()): self.score = 0
        elif (self.hasNumMatchingCards(4)):  self.score = 1
        elif (self.hasGroups(3, 2)):         self.score = 2
        elif (self.isFlush()):               self.score = 3
        elif (self.isStraight()):            self.score = 4
        elif (self.hasNumMatchingCards(3)):  self.score = 5
        elif (self.hasGroups(2, 2)):         self.score = 6
        elif (self.hasNumMatchingCards(2)):  self.score = 7
        else: self.score = 8

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

    def hasGroups(self, size1, size2): # size1 + size2 <= 5
        hand = self.values
        hand = self.removeMatchingCards(hand,size1)
        hand = self.removeMatchingCards(hand,size2)
        if (len(hand) == 5 - size1 - size2):
            return True
        return False

    def hasNumMatchingCards(self, number):
        ranks = []
        for card in self.values:
            ranks.append(card.rank)
        for i in range(1, 13):
            if ranks.count(i) == number:
                return True
        return False

    def removeMatchingCards(self, p_hand, number):
        hand = []
        hand.extend(p_hand)

        ranks = []
        match = 0

        for card in hand:
            ranks.append(card.rank)
        for i in range(1,13):
            if ranks.count(i) == number:
                match = i
        if match != 0:
            for i in range(number):
                ix = ranks.index(match)
                hand.pop(ix)
                ranks.pop(ix)

        return hand

#################################################


def main():
    # get number of hands from user
    handNum = 0
    while handNum == 0 or handNum == None: handNum = intInput()

    data = []
    for i in range(9): data.append([])
    titles = ['Straight Flush','Four of a Kind','Full House','Flush','Straight','Three of a Kind','Two Pairs','One Pair','High Card']
    tabs   = [1,1,2,3,2,0,2,2,2]

    # loop for number of hands
    for h in range(handNum):
        # draw hand
        hand = Hand()
        data[hand.score].append(hand)

    print()
    cache = 'Hands drawn: ' + str(handNum) + '\n\n'

    for i in range(9):
        cache += getScore(titles[i], len(data[i]), handNum, tabs[i])

    print(cache)
    cache = cache.replace('\t',' ')
    writeResults(cache, data, titles)

#-----------------------------------------------

def getScore(title, score, total, tabs = 0):
    return str(title) + ':' + '\t' * tabs + ' ' + str(score) + ' (' + str(score/total*100) + '%)\n'
#-----------------------------------------------
def writeResults(stats, results, titles):
    with open('results.txt', 'w') as f:
        # writes the results to the disk file "results.txt"
        f.write('\nGENERAL STATS:\n\n' + stats + '\n')
        for i in range(len(results)):
            f.write('-' * 20 + '\n\n')
            f.write(titles[i].upper() + ':\n\n')
            if len(results[i]) == 0:
                f.write('No results.\n\n')
                continue
            for hand in results[i]:
                f.write(str(hand)+'; ')
            f.write('\n\n')

def intInput():
    # gets number of hands from user
    try:
        return int(input('Number of hands: '))
    except:
        return None

main()
