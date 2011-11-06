#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Stephen
#
# Created:     06/11/2011
# Copyright:   (c) Stephen 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


class Player:

    def __init__(self, idn, firstname, lastname, leag, gp, minutes, pts, oreb, dreb, reb, asts, stl, blk, turnover, pf, fga, fgm, fta, ftm, tpa, tpm):
#   PARAMETERS
##  *args - strings & ints; each contains a stat of the player

#   VARIABLES
##  val - dictionary; contains the stats

        # initiate a BIG dictionary
        try:
            self.val = {'id': idn, 'firstname': firstname, 'lastname': lastname,        \
            'leag': leag, 'gp': int(gp), 'minutes': int(minutes), 'pts': int(pts),      \
            'oreb': int(oreb), 'dreb': int(dreb), 'reb': int(reb), 'asts': int(asts),   \
            'stl': int(stl), 'blk': int(blk), 'turnover': int(turnover), 'pf': int(pf), \
            'fga': int(fga), 'fgm': int(fgm), 'fta': int(fta), 'ftm': int(ftm),         \
            'tpa': int(tpa), 'tpm': int(tpm) }
        except:
            raise ValueError('Invalid statistical values!')


    def getRank(self, rankType): # returns a rank-value for a given category
#   PARAMETERS
##  rankType - string; the calculation type to perform

#   VARIABLES
##  amt - number; contains the calculated result
##  fga, fta, tpa - numbers; represent their corresponding values, but prevent division by zero

        amt = 0

        if rankType == 'top-players':
            # calculate the value ... a complicated value
            amt = ((self.val['pts'] + self.val['reb'] + self.val['asts'] \
                + self.val['stl'] + self.val['blk']) - ((self.val['fga'] - self.val['fgm']) \
                - (self.val['fta'] - self.val['ftm']) + self.val['turnover'])) / self.val['gp']

        elif rankType == 'top-offensives':
            # prevent division by 0
            fga = self.val['fga'] if self.val['tpm'] != 0 else 1

            # calculate the value
            amt = ((self.val['pts'] + self.val['asts']) - (self.val['turnover'] * 4)) \
            * (self.val['fgm'] / fga)

        elif rankType == 'top-defensives':
            amt = (self.val['dreb'] + (self.val['stl'] * 1.5)) + (self.val['blk'] * 2)

        elif rankType == 'top-scorers':
            amt = self.val['pts']

        elif rankType == 'top-assists':
            amt = self.val['asts']

        elif rankType == 'top-rebounds':
            amt = self.val['reb']

        elif rankType == 'top-steals':
            amt = self.val['stl']

        elif rankType == 'top-blocks':
            amt = self.val['blk']

        elif rankType == 'top-shooters':
            # prevent division by 0
            fga = self.val['fga'] if self.val['tpm'] != 0 else 1
            fta = self.val['fta'] if self.val['fta'] != 0 else 1
            tpa = self.val['tpa'] if self.val['tpa'] != 0 else 1

            # calculate the value
            amt = ((self.val['fgm'] / fga) * 2) + (self.val['ftm'] / fta) \
                + ((self.val['tpm'] / tpa) * 3)

        elif rankType == 'top-3-shooters':
            # prevent division by 0
            tpa = self.val['tpa'] if self.val['tpa'] != 0 else 1

            # calculate the value
            amt = self.val['tpm'] / tpa

        return amt



    def get(self, valueID): # returns a value related to the player
        try:
            return self.val[valueID]
        except:
            return None


def main():
#   VARIABLES
##  stats - list; contains nifty players
##  cmd - string; command intput from user

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


def getInt(prompt):
#   PARAMETERS
## prompt: string, countains user input prompt

    try:
        return int(input(prompt))
    except:
        return None


# displays the menu
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

            data = []
            while True:
                line = file.readline().strip() # current line; whitespace stripped

                if (line == ''): # EOF
                    break

                values = line.split(',') # create list of values

                for j in range(len(values)):
                    if j > 3: # first 4 columns cannot be cast to ints
                        data[columns[j]].append(int(values[j]))
                    else: # these are strings
                        data[columns[j]].append(values[j].strip())

            print('Loaded stats.')
            return data
    except:
        raise IOError('An error occured while loading the file.')
        return None



if __name__ == '__main__':
    main()
