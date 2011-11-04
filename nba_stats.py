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

    cmd = 1
##    showMenu()
##    cmd = getInt('Enter Command: ')

    while cmd != 0:
        print()
        if cmd == 1:
            topPlayers(stats)
        elif cmd == 2:
            topOffensives()
        elif cmd == 3:
            topDefensives()
        elif cmd == 4:
            topScorers()
        elif cmd == 5:
            topAssisters()
        elif cmd == 6:
            topStealers()
        elif cmd == 7:
            topRebounders()
        elif cmd == 8:
            topBlockers()
        elif cmd == 9:
            topShooters()
        elif cmd == 10:
            topThreeShooters()
        else:
            print('Invalid command!')
##
##        showMenu()
##        cmd = getInt('Enter Command: ')
        cmd = 0


def topPlayers(data):
    calc = []
    ids = []

    for i in range(len(data['id'])):
        amt = ((data['pts'][i] + data['reb'][i] + data['asts'][i]\
        + data['stl'][i] + data['blk'][i]) - ((data['fga'][i] - data['fgm'][i])\
        - (data['fta'][i] - data['ftm'][i]) + data['turnover'][i])) / data['gp'][i]

        ids.append(data['id'][i])
        calc.append(amt)

    result = combineAndSort(calc, ids)

    print(topFifty(data, result))


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


def topOffensives():
    pass
def topDefensives():
    pass
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
