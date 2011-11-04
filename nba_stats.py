#
#   NBA Stats
#   Stephen Hoerner
#   CSCD 110
#

import sys

def main():

#   VARIABLES
##  stats - dictionary; contains nifty data
##  cmd - string; command inputed by user

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
            print(getTop(stats, 'top-players'))
        elif cmd == 2:
            print(getTop(stats, 'top-offensives'))
        elif cmd == 3:
            print(getTop(stats, 'top-defensives'))
        elif cmd == 4:
            print(getTop(stats, 'top-scorers'))
        elif cmd == 5:
            print(getTop(stats, 'top-assists'))
        elif cmd == 6:
            print(getTop(stats, 'top-steals'))
        elif cmd == 7:
            print(getTop(stats, 'top-rebounds'))
        elif cmd == 8:
            print(getTop(stats, 'top-blocks'))
        elif cmd == 9:
            print(getTop(stats, 'top-shooters'))
        elif cmd == 10:
            print(getTop(stats, 'top-3-shooters'))
        else:
            print('Invalid command!')

        showMenu()
        cmd = getInt('Enter Command: ')


# returns the top players (in a string) for a given category
def getTop(data,calcType):

#   PARAMETERS
##  data - dictionary; contains all the stat data
##  calcType - string; the category of operation to perform

#   VARIABLES
##  calc - list; contains calculated values
##  ids - list; contains corresponding player IDs
##  index - number; accumulator which represents a player

    calc = []
    ids  = []

    for index in range(len(data['id'])):
        ids.append(data['id'][index])
        calc.append(getCalculation(data, calcType, index))

    return topFifty(data, combineAndSort(calc, ids))



# returns the calculated value for a given index
def getCalculation(dat, calcType, i):

#   PARAMETERS
##  dat - dictionary; contains all the stat data
##  calcType - string; the calculation ID to perform
##  i - int; index value for the current row to operate on

#   VARIABLES
##  amt - number; represents the calculated result
##  fga, fta, tpa - numbers; represent their corresponding values, but prevent division by zero

    amt = 0

    if calcType == 'top-players':
        # calculate the value
        amt = ((dat['pts'][i] + dat['reb'][i] + dat['asts'][i] \
        + dat['stl'][i] + dat['blk'][i]) - ((dat['fga'][i] - dat['fgm'][i]) \
        - (dat['fta'][i] - dat['ftm'][i]) + dat['turnover'][i])) / dat['gp'][i]

    elif calcType == 'top-offensives':
        # prevent division by 0
        fga = dat['fga'][i] if dat['tpm'][i] != 0 else 1

        # calculate the value
        amt = ((dat['pts'][i] + dat['asts'][i]) \
        - (dat['turnover'][i] * 4)) \
        * (dat['fgm'][i] / fga)

    elif calcType == 'top-defensives':
        # calculate the value
        amt = (dat['dreb'][i] + (dat['stl'][i] * 1.5)) \
        + (dat['blk'][i] * 2)

    elif calcType == 'top-scorers':
        # calculate the value
        amt = dat['pts'][i]

    elif calcType == 'top-assists':
        # calculate the value
        amt = dat['asts'][i]

    elif calcType == 'top-steals':
        # calculate the value
        amt = dat['stl'][i]

    elif calcType == 'top-blocks':
        # calculate the value
        amt = dat['blk'][i]

    elif calcType == 'top-shooters':
        # prevent division by 0
        fga = dat['fga'][i] if dat['tpm'][i] != 0 else 1
        fta = dat['fta'][i] if dat['fta'][i] != 0 else 1
        tpa = dat['tpa'][i] if dat['tpa'][i] != 0 else 1

        # calculate the value
        amt = ((dat['fgm'][i] / fga) * 2) \
        + (dat['ftm'][i] / fta) \
        + ((dat['tpm'][i] / tpa) * 3)

    elif calcType == 'top-3-shooters':
        # prevent division by 0
        tpa = dat['tpa'][i] if dat['tpa'][i] != 0 else 1

        # calculate the value
        amt = dat['tpm'][i] / tpa

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

main()
