#
#   NBA Stats
#   Stephen Hoerner
#   CSCD 110
##  (133 lines according to CLOC)
import sys
class Player:

    def __init__(self, vals):
    #   PARAMETERS
    ##  vals (values) - list; contains the player's stats - must have length of 21 or throws exception

    #   VARIABLES
    ##  val - dictionary; contains the stats

        # initiate a BIG dictionary
        try:
            tmpList = ['id','firstname','lastname','leag','gp','minutes','pts','oreb','dreb','reb','asts','stl','blk','turnover','pf','fga','fgm','fta','ftm','tpa','tpm']
            self.val = {}
            for i in range(4):      self.val[tmpList[i]] = str(vals[i]).strip()
            for i in range(4,21):   self.val[tmpList[i]] = int(vals[i])
        except: raise ValueError('Invalid statistical values!')

    def get(self, valueID): # returns a value related to the player
    #   PARAMETERS
    ##  valueID - string; name of the value to return
        try:    return self.val[valueID]
        except: return None

def main():

#   VARIABLES
##  stats - list; contains nifty players
##  cmd - string; command intput from user

    try: stats = loadStats('player_career.txt')
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

        if (cmd == None): print('Invalid command!')
        elif (cmd >= 1 and cmd <= 10 and cmd % 1 == 0): print(getTop(stats, cmd-1)) # is it an int?
        else: print('Invalid command!')

        showMenu()
        cmd = getInt('Enter Command: ')


# returns the top players (via a string) for a given category
def getTop(data, calcType):

#   PARAMETERS
##  data - dictionary; contains all the stat data
##  calcType - int; the index of the operation to perform

#   VARIABLES
##  func - lambda function; used to sort the players
##  safeDiv - lambda function; prevents division by zero
##  output - list; contains players for output
##  i - numbers; accumulator which represents a single player
##  result - string; the accumulator for the resulting data

    output  = data
    safeDiv = lambda n, d: 0 if (d==0) else (n/d)

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

    for i in range(50): result += str(i+1) + '. ' + output[i].get('lastname') + ', ' + output[i].get('firstname') + '\n'   # 'num. name \n'

    return result


def getInt(prompt):
#   PARAMETERS
##  prompt: string; the prompt for user input
    try:    return int(input(prompt))
    except: return None

# displays the menu
def showMenu():
    options = ['players','offensive players','defensive players','scorers','assisters','stealers','rebounders','blockers','shooters','three-point shooters']
    print('\n- - - - - - - - - - - -')
    for opt in range(len(options)):
        print(opt + 1, '.\tList top 50 ', options[opt], sep='')
    print('\n0.\tExit\n- - - - - - - - - - - -\n')


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

                if (line == ''): break  # EOF

                data.append(Player(line.split(','))) # create player with the values

            print('Loaded stats.')
            return data
    except:
        raise IOError('An error occured while loading the file.')
        return None

main()