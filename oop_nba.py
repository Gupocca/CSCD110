#
#   NBA Stats
#   Stephen Hoerner
#   CSCD 110
##  (133 lines according to CLOC)
import sys
class Player:

    def __init__(self, v):
    #   PARAMETERS
    ##  v (values) - list; contains the player's stats - must have length of 21 or throws exception

    #   VARIABLES
    ##  val - dictionary; contains the stats

        # initiate a BIG dictionary
        try:
            tmpList = ['id','firstname','lastname','leag','gp','minutes','pts','oreb','dreb','reb','asts','stl','blk','turnover','pf','fga','fgm','fta','ftm','tpa','tpm']
            self.val = {}
            for i in range(4): self.val[tmpList[i]] = str(v[i]).strip()
            for i in range(4,21): self.val[tmpList[i]] = int(v[i])
        except:
            raise ValueError('Invalid statistical values!')

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

        if cmd == None:
            print('Invalid command!')
        elif cmd >= 1 and cmd <= 10 and cmd % 1 == 0: # is it an int?
            print(getTop(stats, cmd-1))
        else:
            print('Invalid command!')

        showMenu()
        cmd = getInt('Enter Command: ')


# returns the top players (via a string) for a given category
def getTop(data, calcType):

#   PARAMETERS
##  data - dictionary; contains all the stat data
##  calcType - int; the index of the operation to perform

#   VARIABLES
##  func - lambda function; used to sort the players
##  output - list; contains players for output
##  i - numbers; accumulator which represents a single player
##  result - string; the accumulator for the resulting data

    output = data
    func = None

    if   calcType == 0: func = lambda x: safeDiv((x.get('pts')+x.get('reb')+x.get('asts')+x.get('stl')+x.get('blk')-((x.get('fga')-x.get('fgm'))-(x.get('fta')-x.get('ftm'))+x.get('turnover'))), x.get('gp'))
    elif calcType == 1: func = lambda x: ((x.get('pts')+x.get('asts'))-(x.get('turnover')*4))*safeDiv(x.get('fgm'), x.get('fga'))
    elif calcType == 2: func = lambda x: (x.get('dreb')+(x.get('stl')*1.5))+(x.get('blk')*2)
    elif calcType == 3: func = lambda x: x.get('pts')
    elif calcType == 4: func = lambda x: x.get('asts')
    elif calcType == 5: func = lambda x: x.get('reb')
    elif calcType == 6: func = lambda x: x.get('stl')
    elif calcType == 7: func = lambda x: x.get('blk')
    elif calcType == 8: func = lambda x: (safeDiv(x.get('fgm'), x.get('fga'))*2)+safeDiv(x.get('ftm'), x.get('fta'))+(safeDiv(x.get('tpm'), x.get('tpa'))*3)
    elif calcType == 9: func = lambda x: safeDiv(x.get('tpm'), x.get('tpa'))
    else: return None

    output.sort(key=func, reverse=True)
    result = ''

    for i in range(50):
        result += str(i+1) + '. ' + output[i].get('lastname') + ', ' + output[i].get('firstname') + '\n'   # 'num. name \n'

    return result


def getInt(prompt):
#   PARAMETERS
##  prompt: string; the prompt for user input

    try:
        return int(input(prompt))
    except:
        return None

def safeDiv(num, denom):
    return 0 if (denom == 0) else (num / denom)

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

main()