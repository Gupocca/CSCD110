#
#   NBA Stats
#   Stephen Hoerner
#   CSCD 110
#

class Player:

    def __init__(self, v):
    #   PARAMETERS
    ##  v (values) - list; contains the player's stats - must have length of 21 or throws exception

    #   VARIABLES
    ##  val - dictionary; contains the stats

        # initiate a BIG dictionary
        try:
            self.val = { 'id': str(v[0]).strip(), 'firstname': str(v[1]).strip(),               \
            'lastname': str(v[2]).strip(), 'leag': str(v[3]).strip(),       'gp':   int(v[4]),  \
            'minutes':  int(v[5]),  'pts':  int(v[6]),  'oreb': int(v[7]),  'dreb': int(v[8]),  \
            'reb':      int(v[9]),  'asts': int(v[10]), 'stl':  int(v[11]), 'blk':  int(v[12]), \
            'turnover': int(v[13]), 'pf':   int(v[14]), 'fga':  int(v[15]), 'fgm':  int(v[16]), \
            'fta':      int(v[17]), 'ftm':  int(v[18]), 'tpa':  int(v[19]), 'tpm':  int(v[20]) }
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
            amt = self.__shotRate((self.val['pts'] + self.val['reb'] + self.val['asts']     \
                + self.val['stl'] + self.val['blk']) - ((self.val['fga'] - self.val['fgm']) \
                - (self.val['fta'] - self.val['ftm']) + self.val['turnover']), self.val['gp'])

        elif rankType == 'top-offensives':
            amt = ((self.val['pts'] + self.val['asts']) - (self.val['turnover'] * 4))   \
                * self.__shotRate(self.val['fgm'], self.val['fga'])

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
            amt = (self.__shotRate(self.val['fgm'], self.val['fga']) * 2)      \
                + self.__shotRate(self.val['ftm'], self.val['fta'])            \
                + (self.__shotRate(self.val['tpm'], self.val['tpa']) * 3)

        elif rankType == 'top-3-shooters':
            amt = self.__shotRate(self.val['tpm'], self.val['tpa'])

        return amt

    def get(self, valueID): # returns a value related to the player
        try:
            return self.val[valueID]
        except:
            return None

    def __shotRate(self, made, attempted):
        return 0 if (attempted == 0) else (made / attempted)


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


# returns the top players (via a string) for a given category
def getTop(data, calcType):

#   PARAMETERS
##  data - dictionary; contains all the stat data
##  calcType - string; the category of operation to perform

#   VARIABLES
##  output - list; contains tuples in the form (name, rating)
##  name - string; player's name in 'Last, First' format
##  tup - tuple; holds player name and their rating
##  i - numbers; accumulators which represent a single player
##  result - string; the accumulator for the resulting data

    output = []

    for i in range(len(data)):
        name = data[i].get('lastname') + ', ' + data[i].get('firstname')
        tup = (name, data[i].getRank(calcType))
        output.append(tup)

    output.sort(key = lambda val: val[1], reverse = True)
    result = ''

    for i in range(50):
        result += str(i+1) + '. ' + output[i][0] + ' \t - ' + str(output[i][1]) + '\n'   # 'num. name \n'

    return result


def getInt(prompt):
#   PARAMETERS
##  prompt: string; the prompt for user input

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
##  filename - string; file to open

#   VARIABLES
##  file - handle; the file
##  data - list; accumulates Player()'s
##  line - string; contains the value of a line

    try:
        with open(filename, 'r') as file:
            file.readline() # skip the first line
            data = []

            while True:
                line = file.readline().strip() # current line; whitespace stripped

                if (line == ''): # EOF
                    break

                data.append(Player(line.split(','))) # create player with the values

            print('Loaded stats.')
            return data
    except:
        raise IOError('An error occured while loading the file.')
        return None


if __name__ == '__main__':
    main()
