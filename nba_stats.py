#-------------------------------------------------------------------------------
# Name:        NBA Stats
#
# Author:      Stephen Hoerner
#
# Created:     04/11/2011
# Copyright:   (c) Stephen Hoerner 2011
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys

def main():
    try:
        stats = loadStats('player_career.txt')
    except IOError as e:
        print(e)
        sys.exit(0)
    except:
        print('An unknown error occured.')
        sys.exit(0)

    # menu selection

    showMenu()
    cmd = getInt('Enter Command: ')

    while cmd != 0:
        print()
        if cmd == 1:
            print(topPlayers(stats))
        elif cmd == 2:
            print(topOffensives(stats))
        elif cmd == 3:
            print(topDefensives(stats))
        elif cmd == 4:
            print(topScorers())
        elif cmd == 5:
            print(topAssisters())
        elif cmd == 6:
            print(topStealers())
        elif cmd == 7:
            print(topRebounders())
        elif cmd == 8:
            print(topBlockers())
        elif cmd == 9:
            print(topShooters())
        elif cmd == 10:
            print(topThreeShooters())
        else:
            print('Invalid command!')
##
##        showMenu()
##        cmd = getInt('Enter Command: ')
        cmd = 0


def topPlayers(data):
##    calc = []
##    ids = []
##
##    for i in range(len(data['id'])):
##        amt = ((data['pts'][i] + data['reb'][i] + data['asts'][i]\
##        + data['stl'][i] + data['blk'][i]) - ((data['fga'][i] - data['fgm'][i])\
##        - (data['fta'][i] - data['ftm'][i]) + data['turnover'][i])) / data['gp'][i]
##
##        ids.append(data['id'][i])
##        calc.append(amt)
##
##    result = combineAndSort(calc, ids)
##    return topFifty(data, result)
    return topFifty(data, getStuff(data,'top-players'))

def topOffensives(data):
    calc = []
    ids = []

    for i in range(len(data['id'])):
        fga = data['fga'][i]
        if fga == 0:
            fga = -1

        amt = ((data['pts'][i] + data['asts'][i]) \
        - (data['turnover'][i] * 4)) \
        * (data['fgm'][i] / fga)

        ids.append(data['id'][i])
        calc.append(amt)

    result = combineAndSort(calc, ids)
    return topFifty(data, result)

def topDefensives(data):
    calc = []
    ids = []

    for i in range(len(data['id'])):


        ids.append(data['id'][i])
        calc.append(amt)

    result = combineAndSort(calc, ids)
    return topFifty(data, result)



def getStuff(data,calcType):
    calc = []
    ids = []

    for index in range(len(data['id'])):
        amt = getCalculation(data, calcType, index)

        ids.append(data['id'][index])
        calc.append(amt)

    return combineAndSort(calc, ids)


def getCalculation(data, calcType, i):
    amt = 0
    if calcType == 'top-players':
        amt = ((data['pts'][i] + data['reb'][i] + data['asts'][i]\
        + data['stl'][i] + data['blk'][i]) - ((data['fga'][i] - data['fgm'][i])\
        - (data['fta'][i] - data['ftm'][i]) + data['turnover'][i])) / data['gp'][i]

    elif calcType == 'top-offensives':
        fga = data['fga'][i]
        if fga == 0:
            fga = -1

        amt = ((data['pts'][i] + data['asts'][i]) \
        - (data['turnover'][i] * 4)) \
        * (data['fgm'][i] / fga)

    elif calcType == 'top-defensives':
        amt = (data['dreb'][i] + (data['stl'][i] * 1.5)) \
        + (data['blk'][i] * 2)

    elif calcType == 'top-scorers':
        pass
    elif calcType == 'top-assists':
        pass
    elif calcType == 'top-steals':
        pass
    elif calcType == 'top-blocks':
        pass
    elif calcType == 'top-shooters':
        pass
    elif calcType == 'top-3-shooters':
        pass
    else:
        pass
    return amt

def topScorers():
    pass
def topAssisters():
    pass
def topStealers():
    pass
def topRebounders():
    pass
def topBlockers():
    pass
def topShooters():
    pass
def topThreeShooters():
    pass

def combineAndSort(valueList, keyList):
    result = list(zip(valueList, keyList))
    result.sort()
    result.reverse()

    for i in range(len(result)):
        result[0] = list(result[0])

    return result


def topFifty(data, lst):
    output = ''

    for i in range(50):
        tempID = data['id'].index(lst[i][1])
        output += str(i+1) + '. ' + data['firstname'][tempID] + ' ' + data['lastname'][tempID] + '\n'

    return output

def getInt(prompt):
    ## prompt: string, countains user input prompt

    try:
        return int(input(prompt))
    except:
        return None


def showMenu():
    print()
    print('- - - - - - - - - - - -')
    print('1. List top 50 players')
    print('2. List top 50 offensive players')
    print('3. List top 50 defensive players')
    print('4. List top 50 scorers')
    print('5. List top 50 assisters')
    print('6. List top 50 stealers')
    print('7. List top 50 rebounders')
    print('8. List top 50 blockers')
    print('9. List top 50 shooters')
    print('10. List top 50 three-point shooters')
    print()
    print('0. exit')
    print('- - - - - - - - - - - -')
    print()


def loadStats(filename):
    try:
        with open(filename, 'r') as file:
            file.readline() # skip the first line

            columns = ['id','firstname','lastname','leag','gp','minutes','pts','oreb','dreb',\
            'reb','asts','stl','blk','turnover','pf','fga','fgm','fta','ftm','tpa','tpm']

            data = {}

            for id in columns:
                data[id] = []

            while True:
                line = file.readline().strip()

                if (line == ''):
                    break

                line = line.split(',')

                for j in range(len(line)):
                    if j > 3:
                        data[columns[j]].append(int(line[j]))
                    else:
                        data[columns[j]].append(line[j].strip())

            print('Loaded stats.')
            return data
    except:
        raise IOError('An error occured while loading the file.')
        return None


if __name__ == '__main__':
    main()
