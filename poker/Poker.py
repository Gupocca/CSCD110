# this allows for direct addressing Card() instead of Card.Card() construction
from Card import *
import re

def main():
    # your main will look totally different
    # this is for testing the Card class from Card.py
    # it should shuffle a random deck of cards
##
##
##    hnd = []
##    for i in range(52):
##        potential = Card()
##        while potential in hnd:
##            potential = Card()
##        hnd.append(potential)
##    print("Random:",hnd)
##    hnd.sort()
##    print("Sorted:",hnd)


    # skeleton for your main

    # get number of hands from user
    handNum = 0
    while handNum == 0 or handNum == None:
        handNum = intInput()

    # initialize accumulator variables for each hand scoring category
    score = {'straightFlush': 0, 'fourOfAKind': 0, 'fullHouse': 0, 'flush': 0, 'straight': 0, 'threeOfAKind': 0, 'twoPairs': 0, 'onePair': 0, 'highCard': 0}
    data  = {'straightFlush': [], 'fourOfAKind': [], 'fullHouse': [], 'flush': [], 'straight': [], 'threeOfAKind': [], 'twoPairs': [], 'onePair': [], 'highCard': []}

    # loop for number of hands
    for h in range(handNum):
        # draw hand
        hand = DrawHand()

        # send hand to scoring methods
        if isStraightFlush(hand):  score['straightFlush'] += 1; data['straightFlush'].append(hand)
        elif isFourOfAKind(hand):  score['fourOfAKind']   += 1; data['fourOfAKind'].append(hand)
        elif isFullHouse(hand):    score['fullHouse']     += 1; data['fullHouse'].append(hand)
        elif isFlush(hand):        score['flush']         += 1; data['flush'].append(hand)
        elif isStraight(hand):     score['straight']      += 1; data['straight'].append(hand)
        elif isThreeOfAKind(hand): score['threeOfAKind']  += 1; data['threeOfAKind'].append(hand)
        elif isTwoPair(hand):      score['twoPairs']      += 1; data['twoPairs'].append(hand)
        elif isOnePair(hand):      score['onePair']       += 1; data['onePair'].append(hand)
        elif isHighCard(hand):     score['highCard']      += 1; data['highCard'].append(hand)

    print()
    cache = 'Hands drawn: ' + str(handNum) + '\n\n'

    cache += getScore('Straight Flush',  score['straightFlush'], handNum, 1)
    cache += getScore('Four of a Kind',  score['fourOfAKind'],   handNum, 1)
    cache += getScore('Full House',      score['fullHouse'],     handNum, 2)
    cache += getScore('Flush',           score['flush'],         handNum, 3)
    cache += getScore('Straight',        score['straight'],      handNum, 2)
    cache += getScore('Three of a Kind', score['threeOfAKind'],  handNum)
    cache += getScore('Two Pairs',       score['twoPairs'],      handNum, 2)
    cache += getScore('One Pair',        score['onePair'],       handNum, 2)
    cache += getScore('High Card',       score['highCard'],      handNum, 2)

    print(cache)
    cache = cache.replace('\t',' ')
    writeResults(cache, data)

    # Print out results for each scoring category and the total number of hands drawn
    # format:
    #           Total number of Hands Drawn: 100,000
    #
    #          Straight Flush: X (xx%)
    #          Four of a Kind: X (xx%)
    #          Full House:     X (xx%)
    #           etc...
    #

def getScore(title, score, total, tabs = 0):
    return str(title) + ':' + '\t' * tabs + str(score) + ' (' + str(score/total*100) + '%)\n'

def DrawHand():
    # randomly draw hand, ensure not duplicates, returns hand to main
    hand = []
    for c in range(5):
        card = Card()
        while card in hand: # must be unique
            card = Card()
        hand.append(card)
    return hand

# You will need to populate the following functions to determine what the top
# scoring category for your hands are.
# Remember, check these in the highest scoring hand to the lowest.  Otherwise,
# you will incorrectly pick the scoring category.
def isStraightFlush(hand):
    hand.sort()

    for c in range(5):
        if not hand[c].isSameSuit(hand[0]):
            return False
        if hand[c].rank != hand[0].rank + c:
            return False

    #print("Straight Flush:", hand)
    return True
    # returns True if straight flush, otherwise False



def isFourOfAKind(hand):
    return hasNumMatchingCards(hand, 4)
    # returns True if Four of a Kind, otherwise False


def isFullHouse(hand):
##    ranks = []
##    flag = False
##    tmpHand = hand
##
##    if (hasNumMatchingCards(hand, 2))
##
##    return True

    tmpHand = []
    tmpHand.extend(hand)

    tmpHand = removeMatchingCards(tmpHand,3)
    tmpHand = removeMatchingCards(tmpHand,2)

    if (len(tmpHand) == 0):
        #print(hand)
        return True

    return False

def hasNumMatchingCards(hand, number):
    ranks = []
    for card in hand:
        ranks.append(card.rank)
    for i in range(1,13):
        if ranks.count(i) == number:
            return True
    return False

def removeMatchingCards(hand, number):
    ranks = []
    match = 0

    for card in hand:
        ranks.append(card.rank)
    for i in range(1,13):
        if ranks.count(i) == number:
            match = i

    if match == 0:
        return hand

    for i in range(number):
        hand.remove(hand[ranks.index(match)])

    return hand

def isFlush(hand):
    for i in range(len(hand)-1):
        if hand[i].suit != hand[i+1].suit:
            return False
    return True
    # returns True if Flush, otherwise False

def isStraight(hand):
    for c in range(5):
        if hand[c].rank != hand[0].rank + c:
            return False
    return True

def isThreeOfAKind(hand):
    return hasNumMatchingCards(hand, 3)
    # returns True if Three of a Kind, otherwise False

def isTwoPair(hand):
    tmpHand = []
    tmpHand.extend(hand)

    tmpHand = removeMatchingCards(tmpHand,2)
    tmpHand = removeMatchingCards(tmpHand,2)

    if len(tmpHand) == 1:
        return True

    return False
    # returns True if Two Pair, otherwise False


def isOnePair(hand):
    return hasNumMatchingCards(hand, 2)

def isHighCard(hand):
    hand.sort()
    ## hand[4]
    return True
#-----------------------------------------------
def writeResults(stats, results):
    with open('results.txt', 'w') as f:
        # writes the results to the disk file "results.txt"
        f.write('\nGENERAL STATS:\n\n' + stats + '\n')
        for key in results.keys():
            f.write('-' * 20 + '\n\n')
            title = re.sub("([A-Z])"," \g<0>", key)
            f.write(title.upper() + ':\n\n')
            if len(results[key]) == 0:
                f.write('No results.\n\n')
                continue
            for hand in results[key]:
                f.write(str(hand)+'; ')
            f.write('\n\n')

def intInput():
    # gets number of hands from user
    try:
        return int(input('Number of hands: '))
    except:
        return None
    pass


main()
