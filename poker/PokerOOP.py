from Card import *

class Hand():
    def __init__(self):
        self.values = [] # create value list

        for c in range(5): # draw hand
            card = Card()
            while card in self.values: # must be unique
                card = Card()
            self.values.append(card) # add to list

        self.values.sort()
        self.score = self.getHighestType() # get the score

    def __str__(self):
        return str(self.values) # return the value list

    def getHighestType(self):
        if (self.isStraight() and self.isFlush()): return 0 # straight flush
        elif (self.hasNumMatchingCards(4)):  return 1 # four of a kind
        elif (self.hasGroups(3, 2)):         return 2 # full house
        elif (self.isFlush()):               return 3 # flush
        elif (self.isStraight()):            return 4 # straight
        elif (self.hasNumMatchingCards(3)):  return 5 # three of a kind
        elif (self.hasGroups(2, 2)):         return 6 # two pairs
        elif (self.hasNumMatchingCards(2)):  return 7 # one pair
        else: return 8 # high card

    def isFlush(self):
        for i in range(5): # all cards must have the same suit as the first
            if not self.values[i].isSameSuit(self.values[0]):
                return False
        return True

    def isStraight(self):
        for i in range(5): # loop through values, check for pattern like: [1,2,3,4,5]
            if self.values[i].rank != self.values[0].rank + i:
                return False
        return True

    def hasGroups(self, size1, size2): # size1 + size2 <= 5
        hand = self.removeMatchingCards(self.values, size1) # a group
        hand = self.removeMatchingCards(hand, size2) # removes another

        # if both were removed w/ success, then the len() should equal...
        if (len(hand) == 5 - size1 - size2):
            return True

        return False

    def hasNumMatchingCards(self, number):
        ranks = []
        for card in self.values: # add ranks to list
            ranks.append(card.rank)
        for i in range(1, 13): # find a match
            if ranks.count(i) >= number:
                return True
        return False

    def removeMatchingCards(self, p_hand, number):
        hand = []
        hand.extend(p_hand)

        ranks = []
        match = 0

        for card in hand: # enumerate through cards and add ranks to list
            ranks.append(card.rank)
        for i in range(1, 13): # enumerate through numbers to find exact match
            if ranks.count(i) >= number:
                match = i
        if match != 0: # found result
            for i in range(number): # only removes first x results for precision
                ix = ranks.index(match)
                hand.pop(ix)
                ranks.pop(ix)

        return hand

#################################################


def main():
    # get number of hands from user
    handNum = 0
    # ensure that the number is valid
    while (handNum == 0 or handNum == None): handNum = intInput()

    data = []
    for i in range(9): data.append([]) # create 9 sublists
    titles = ['Straight Flush','Four of a Kind','Full House','Flush','Straight','Three of a Kind','Two Pairs','One Pair','High Card']

    # loop for number of hands
    for h in range(handNum):
        hand = Hand() # draw hand
        data[hand.score].append(hand) # add hand to correct score sublist

    cache = 'Hands drawn: ' + str(handNum) + '\n\n' # begin the cache

    for i in range(9):  # add each data data score to the output cache
        cache += getScore(titles[i], len(data[i]), handNum, [1,1,2,3,2,0,2,2,2][i]) # list at the end contains "tab #s" for display

    print('\n' + cache) # print cache to screen
    cache = cache.replace('\t',' ') # remove tabs for file formatting
    writeResults(cache, data, titles) # write to file

#-----------------------------------------------

def getScore(title, score, total, tabs = 0):
    # returns formatted score -- "title: number (percent %)"
    return str(title) + ':' + '\t' * tabs + ' ' + str(score) + ' (' + str(score/total*100) + '%)\n'
#-----------------------------------------------
def writeResults(stats, results, titles):
    with open('results.txt', 'w') as f:
        # general statistics (percentages)
        f.write('\nGENERAL STATS:\n\n' + stats + '\n')
        # loop through each score type
        for i in range(len(results)):
            f.write('-' * 20 + '\n\n') # separator
            f.write(titles[i].upper() + ':\n\n') # title in uppercase
            if len(results[i]) == 0: # empty list
                f.write('No results.\n\n')
                continue
            for hand in results[i]: # print hands
                f.write(str(hand)+'; ')
            f.write('\n\n')

def intInput():
    # gets number of hands from user
    try:
        return int(input('Number of hands: '))
    except:
        return None

main()
