from Card import *

def main():
    handNum = 0
    while (handNum == 0 or handNum == None): handNum = intInput()

    data = [0,0,0,0,0,0,0,0,0]
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
    vals = [] # create value list

    for c in range(5): # draw hand
        card = Card()
        while card in vals: # must be unique
            card = Card()
        vals.append(card) # add to list

    vals.sort(key=lambda x: x.sortKey())
    return vals


def isFlush(hand):
    for i in range(5): # all cards must have the same suit as the first
        if not hand[i].isSameSuit(hand[0]):
            return False
    return True

def isStraight(hand):
    return ((hand[1].rank == hand[0].rank + 1) and (hand[2].rank == hand[1].rank + 1) and \
    (hand[3].rank == hand[2].rank + 1) and (hand[4].rank == hand[3].rank + 1)) or \
    ((hand[0].rank == 1) and (hand[2].rank == hand[1].rank + 1) and \
    (hand[3].rank == hand[2].rank + 1) and (hand[4].rank == hand[3].rank + 1) \
    and (14 == hand[4].rank + 1))


def hasNumMatchingCards(hand, number):
    ranks = []
    for card in hand: # add ranks to list
        ranks.append(card.rank)
    for i in range(1, 13): # find a match
        if ranks.count(i) >= number:
            return True
    return False

def hasGroups(hand, size1, size2): # size1 + size2 <= 5
    if size1 < size2:
        size1, size2 = size2, size1

    hnd = removeMatchingCards(hand, size1) # a group
    hnd = removeMatchingCards(hnd, size2) # removes another

    # if both were removed w/ success, then the len() should equal...
    if (len(hnd) == 5 - size1 - size2):
        return True

    return False


def removeMatchingCards(hand, number):
    hnd = []
    hnd.extend(hand)

    ranks = []
    match = 0

    for card in hand: # enumerate through cards and add ranks to list
        ranks.append(card.rank)
    for i in range(1, 13): # enumerate through numbers to find exact match
        if ranks.count(i) >= number:
            match = i
    if match != 0: # found result
        for i in range(number): # only removes first x results for precision
            ix=ranks.index(match)
            hnd.pop(ix)
            ranks.pop(ix)

    return hnd




def getScore(title, score, total, tabs = 0):
    # returns formatted score -- "title: number (percent %)"
    return str(title) + ':' + '\t' * tabs + ' ' + str(score) + ' (' + str(score/total*100) + '%)\n'
#-----------------------------------------------
def writeResults(stats):
    try:
        with open('results.txt', 'a') as f:
            # general statistics (percentages)
            f.write('\n[' + str(datetime.datetime.now())  +']\n')
            f.write('\nRESULTS:\n\n' + stats + '\n' + '-' * 20 + '\n')
    except:
        print('Unable to write to file')

def intInput():
    # gets number of hands from user
    try:
        return int(input('Number of hands: '))
    except:
        return None



def tester():
    h = drawHand()
    h[0].rank = 11
    h[1].rank = 11
    h[2].rank = 12
    h[3].rank = 12
    h[4].rank = 12
    print(hasGroups(h,2,3))

main()
##print('\n')
##tester()