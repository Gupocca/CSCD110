# this allows for direct addressing Card() instead of Card.Card() construction
from Card import *

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
    score = {}

    score['straightFlush']  = 0
    score['fourOfKind']     = 0
    score['fullHouse']      = 0
    score['flush']          = 0
    score['threeOfKind']    = 0
    score['twoPair']        = 0
    score['onePair']        = 0


    # loop for number of hands
    for h in range(handNum):
        # draw hand
        hand = DrawHand()

        # send hand to scoring methods
        if isStraightFlush(hand):  score['straightFlush'] += 1
        elif isFourOfAKind(hand):  score['fourOfKind']    += 1
        elif isFullHouse(hand):    score['fullHouse']     += 1
        elif isFlush(hand):        score['flush']         += 1
        elif isThreeOfAKind(hand): score['threeOfKind']   += 1
        elif isTwoPair(hand):      score['twoPair']       += 1
        elif isOnePair(hand):      score['onePair']       += 1

    print('Total number of Hands Drawn:', handNum)
    print()
    printScore('Straight Flush',  score['straightFlush'], handNum, 1)
    printScore('Four of a Kind',  score['fourOfKind'],    handNum, 1)
    printScore('Full House',      score['fullHouse'],     handNum, 2)
    printScore('Flush',           score['flush'],         handNum, 3)
    printScore('Three of a Kind', score['threeOfKind'],   handNum)
    printScore('Two Pairs',       score['twoPair'],       handNum, 2)
    printScore('One Pair',        score['onePair'],       handNum, 2)


    # Print out results for each scoring category and the total number of hands drawn
    # format:
    #           Total number of Hands Drawn: 100,000
    #
    #          Straight Flush: X (xx%)
    #          Four of a Kind: X (xx%)
    #          Full House:     X (xx%)
    #           etc...
    #

def printScore(title, score, total, tabs = 0):
    print(str(title) + ':' + '\t' * tabs, score, '(' + str(score/total*100) + '%)')

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

    print("Straight Flush:", hand)
    return True
    # returns True if straight flush, otherwise False
    pass
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
        print(hand)
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

def isThreeOfAKind(hand):
    return hasNumMatchingCards(hand, 3)
    # returns True if Three of a Kind, otherwise False

def isTwoPair(hand):
    # returns True if Two Pair, otherwise False
    pass
def isOnePair(hand):
    # returns True if One Pair, otherwise False
    pass
#-----------------------------------------------
def writeResults():
    # writes the results to the disk file "results.txt"
    pass
def intInput():
    # gets number of hands from user
    try:
        return int(input('Number of hands: '))
    except:
        return None
    pass


main()
