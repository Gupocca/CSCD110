from Card import *
import datetime

def main():
##  handNum: int; number of times to draw hands
##  data: list of ints; accumulator variable for successes
##  titles: list of strings; used when printing results
##  irrelevantLittleNumber: int; a poor yet oft-used iterator that we never even check the value of
##  cache: string; accumulates the final results for printing

    handNum = 0
    while (handNum == 0 or handNum == None): handNum = intInput()

    data = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    titles = ['Straight Flush','Four of a Kind','Full House','Flush','Straight','Three of a Kind','Two Pairs','One Pair','High Card']

    for irrelevantLittleNumber in range(handNum + 1):
        hand = drawHand()

        if (isStraight(hand) and isFlush(hand)): data[0] += 1 # straight flush
        elif (hasNumMatchingCards(hand, 4)):     data[1] += 1 # four of a kind
        elif (hasGroups(hand, 3, 2)):            data[2] += 1 # full house
        elif (isFlush(hand)):                    data[3] += 1 # flush
        elif (isStraight(hand)):                 data[4] += 1 # straight
        elif (hasNumMatchingCards(hand, 3)):     data[5] += 1 # three of a kind
        elif (hasGroups(hand, 2, 2)):            data[6] += 1 # two pairs
        elif (hasNumMatchingCards(hand, 2)):     data[7] += 1 # one pair
        else: data[8] += 1 # high card

    cache = 'Hands drawn: ' + str(handNum) + '\n\n'
    for i in range(9):
        cache += getScore(titles[i], data[i], handNum, [1,1,2,3,2,0,2,2,2][i]) # list at the end contains "tab #s" for display

    print('\n' + cache) # print cache to screen
    cache = cache.replace('\t',' ') # remove tabs for file formatting
    writeResults(cache) # write to file


def drawHand():
##  vals: list of cards; accumulates cards and should result in a 5-card hand
##  c: int; simple iterative variable
##  card: Card; potential card for the hand

    vals = [] # create value list

    for c in range(5): # draw hand
        card = Card()
        while card in vals: # must be unique
            card = Card()
        vals.append(card) # add to list

    vals.sort(key = lambda x: x.sortKey())
    return vals


def isFlush(hand): # returns: boolean
##  hand (param): list of cards; represents a 5-card hand
##  i: int; iterative variable

    for i in range(5): # all cards must have the same suit as the first
        if not hand[i].isSameSuit(hand[0]):
            return False
    return True

def isStraight(hand): # returns: boolean
##  hand (param): list of cards; represents a 5-card hand

    return ((hand[1].rank == hand[0].rank + 1) and (hand[2].rank == hand[1].rank + 1) and \
    (hand[3].rank == hand[2].rank + 1) and (hand[4].rank == hand[3].rank + 1)) or \
    ((hand[0].rank == 1) and (hand[2].rank == hand[1].rank + 1) and \
    (hand[3].rank == hand[2].rank + 1) and (hand[4].rank == hand[3].rank + 1) \
    and (14 == hand[4].rank + 1))


def hasNumMatchingCards(hand, number): # returns: boolean
##  hand (param): list of cards; represents a 5-card hand
##  number (param): int; minimum number of cards that have the same rank
##  ranks: list of ints; contains the numerical ranks of the cards
##  card: Card; member of the given hand - used to get a rank

    ranks = getRanks(hand)
    for i in range(1, 13): # find a match
        if ranks.count(i) >= number:
            return True
    return False

def hasGroups(hand, size1, size2): # returns: boolean
##  hand (param): list of cards; represents a 5-card hand
##  size1 & size2 (params): ints; the size of 2 "groups" of similarly-ranked cards which the hand should contain
##  hnd: list of cards; variable in place of "hand" so as to be non-destructive to the parameter

    if size1 < size2: # function works much better if larger num is checked before smaller num
        size1, size2 = size2, size1 # ... so swap them if necessary

    hnd = removeMatchingCards(hand, size1) # removes a card group of size 'size1'
    hnd = removeMatchingCards(hnd, size2)  # removes another of size 'size2'

    # if both were removed w/ success, then the len() should equal...
    if (len(hnd) == 5 - size1 - size2):
        return True

    return False


def removeMatchingCards(hand, number): # returns: list of cards ('hand')
##  hand (param): list of cards; represents a 5-card hand
##  hnd: list of cards; temporary variable cloned from "hand"
##  ranks: list of ints; contains the numerical ranks of the cards
##  match: int; if a match is made, this is the single 'rank' of the included cards
##  i (used twice): int; simple iterator variable

    hnd = []
    hnd.extend(hand)

    ranks = getRanks(hand)
    match = 0

    for i in range(1, 13): # enumerate through numbers to find exact match
        if ranks.count(i) >= number:
            match = i
    if match != 0: # found result
        for i in range(number): # only removes first x results for precision
            hnd.pop(ranks.index(match))
            ranks.pop(ranks.index(match))

    return hnd

def getRanks(hand): # returns: list of ints
##  hand (param): list of cards; represents a 5-card hand
##  ranks: list of ints; contains the numerical ranks of the cards

    ranks = []
    for card in hand: # add ranks to list
        ranks.append(card.rank)
    return ranks


def getScore(title, score, total, tabs = 0): # returns: string
##  title (param): string; title for the result
##  score (param): int; number of successes
##  total (param): int; number of tries
##  tabs (param): int; number of tabs (just to make it look pretty)

    # returns formatted score -- "title: number (percent %)"
    return str(title) + ':' + '\t' * tabs + ' ' + str(score) + ' (' + str(score/total*100) + '%)\n'


def writeResults(stats):
##  stats (param): string; the stuff we write to the file
    try:
        # general statistics (percentages)
        with open('results.txt', 'a') as f:
            f.write('\n[' + str(datetime.datetime.now())  +']\n')
            f.write('\nRESULTS:\n\n' + stats + '\n' + '-' * 20 + '\n')
    except:
        print('Unable to write to file!')

def intInput():
    # get number of hands from user
    try:
        return int(input('Number of hands: '))
    except:
        return None

main()