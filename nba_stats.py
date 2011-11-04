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
            print(topScorers(stats))
        elif cmd == 5:
            print(topAssisters(stats))
        elif cmd == 6:
            print(topStealers(stats))
        elif cmd == 7:
            print(topRebounders(stats))
        elif cmd == 8:
            print(topBlockers(stats))
        elif cmd == 9:
            print(topShooters(stats))
        elif cmd == 10:
            print(topThreeShooters(stats))
        else:
            print('Invalid command!')

        showMenu()
        cmd = getInt('Enter Command: ')


def topPlayers(data): # returns top fifty players
    return topFifty(data, getTop(data,'top-players'))

def topOffensives(data): # returns top fifty offensive players
    return topFifty(data, getTop(data,'top-offensives'))

def topDefensives(data): # returns top fifty defensive players
    return topFifty(data, getTop(data,'top-defensives'))

def topScorers(data): # returns top fifty players for scoring
    return topFifty(data, getTop(data,'top-scorers'))

def topAssisters(data): # returns top fifty players for assisting
    return topFifty(data, getTop(data,'top-assists'))

def topStealers(data): # returns top fifty players for stealing
    return topFifty(data, getTop(data,'top-steals'))

def topRebounders(data): # returns top fifty players for rebounding
    return topFifty(data, getTop(data,'top-rebounds'))

def topBlockers(data): # returns top fifty players for blocking
    return topFifty(data, getTop(data,'top-blocks'))

def topShooters(data): # returns top fifty players for shooting
    return topFifty(data, getTop(data,'top-shooters'))

def topThreeShooters(data): # returns top fifty players for shooting 3-pointers
    return topFifty(data, getTop(data,'top-3-shooters'))

# returns a list of the best players for a given category
def getTop(data,calcType):

#   PARAMETERS
##  data - dictionary; contains all the stat data
##  calcType - string; the category of operation to perform

#   VARIABLES
##  calc - list; contains calculated values
##  ids - list; contains corresponding player IDs
##  index - number; accumulator which represents a player

    calc = []
    ids = []

    for index in range(len(data['id'])):
        ids.append(data['id'][index])
        calc.append(getCalculation(data, calcType, index))

    return combineAndSort(calc, ids)



# returns the calculated value for a given index
def getCalculation(data, calcType, i):

#   PARAMETERS
##  data - dictionary; contains all the stat data
##  calcType - string; the calculation ID to perform
##  i - int; index value for the current row to operate on

#   VARIABLES
##  amt - number; represents the calculated result
##  fga, fta, tpa - numbers; represent their corresponding values, but prevent division by zero

    amt = 0

    if calcType == 'top-players':
        amt = ((data['pts'][i] + data['reb'][i] + data['asts'][i]\
        + data['stl'][i] + data['blk'][i]) - ((data['fga'][i] - data['fgm'][i])\
        - (data['fta'][i] - data['ftm'][i]) + data['turnover'][i])) / data['gp'][i]

    elif calcType == 'top-offensives':
        # prevent division by 0
        fga = data['fga'][i] if data['tpm'][i] != 0 else -0.1

        amt = ((data['pts'][i] + data['asts'][i]) \
        - (data['turnover'][i] * 4)) \
        * (data['fgm'][i] / fga)

    elif calcType == 'top-defensives':
        amt = (data['dreb'][i] + (data['stl'][i] * 1.5)) \
        + (data['blk'][i] * 2)

    elif calcType == 'top-scorers':
        amt = data['pts'][i]

    elif calcType == 'top-assists':
        amt = data['asts'][i]

    elif calcType == 'top-steals':
        amt = data['stl'][i]

    elif calcType == 'top-blocks':
        amt = data['blk'][i]

    elif calcType == 'top-shooters':
        # prevent division by 0
        fga = data['fga'][i] if data['tpm'][i] != 0 else -0.1
        fta = data['fta'][i] if data['fta'][i] != 0 else -0.1
        tpa = data['tpa'][i] if data['tpa'][i] != 0 else -0.1

        amt = ((data['fgm'][i] / fga) * 2) \
        + (data['ftm'][i] / fta) \
        + ((data['tpm'][i] / tpa)*3)

    elif calcType == 'top-3-shooters':
        # prevent division by 0
        tpa = data['tpa'][i] if data['tpa'][i] != 0 else -0.1

        amt = data['tpm'][i] / tpa

    ## end calculations
    return amt



# takes two lists, sorts them by valueList, and returns
# one list containing sub-lists in the form [value, key]
def combineAndSort(valueList, keyList):

#   PARAMETERS
##  valueList - list; a list to sort by
##  keyList - list; a list with identifiers

#   VARIABLES
##  result - list; contains final results
##  i - number; simple accumulator index

    result = list(zip(valueList, keyList))
    result.sort()
    result.reverse()

    for i in range(len(result)):
        result[0] = list(result[0])

    return result


# returns the first fifty player names in a given ID-list
def topFifty(data, lst):

#   PARAMETERS
##  data - dictionary; contains all the stat data
##  lst - list; contains player ID's in whatever order desired

#   VARIABLES
##  output - string; contains output...
##  tempID - string; holds a temporary player ID

    output = ''

    for i in range(50):
        tempID = data['id'].index(lst[i][1])
        output += str(i+1) + '. ' + data['firstname'][tempID] + ' ' + data['lastname'][tempID] + '\n'

    return output



# gets an int from the user
def getInt(prompt):

#   PARAMETERS
## prompt: string, countains user input prompt

    try:
        return int(input(prompt))
    except:
        return None



# displaysthe menu
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



# loads the player statistics from a given filename
def loadStats(filename):

#   PARAMETERS
##  filename - string; the file to open

#   VARIABLES
##  file - handle; represents the file
##  columns - list; the columns to use
##  data - dictionary; accumulates all the data
##  line - string; contains the value of a line
##  values - list; contains individual values of a list

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

                values = line.split(',')

                for j in range(len(values)):
                    if j > 3:
                        data[columns[j]].append(int(values[j]))
                    else:
                        data[columns[j]].append(values[j].strip())

            print('Loaded stats.')
            return data
    except:
        raise IOError('An error occured while loading the file.')
        return None


if __name__ == '__main__':
    main()
