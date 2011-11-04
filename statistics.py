## Stephen Hoerner
## Assignment #4
## CSCD 110

# main program
def main():
    ## values:  list, contains the values
    ## cmd:     number, command index given by user

    values = []

    showMenu()
    cmd = inputNum('Enter Command: ')

    while cmd != 0:
        print()
        if cmd == 1:
            showList(values)

        elif cmd == 2:
            values = addNum(values)

        elif cmd == 3:
            values = delNum(values)

        elif cmd == 4:
            values = purgeList(values)

        elif cmd == 5:
            print(getMean(values))

        elif cmd == 6:
            print(getMidRange(values))

        elif cmd == 7:
            print(getMedian(values))

        elif cmd == 8:
            showList(getMode(values))

        else:
            print('Invalid command!')

        showMenu()
        cmd = inputNum('Enter Command: ')


# displays a menu for commands
def showMenu():
    print()
    print('- - - - - - - - - - - -')
    print('1. display numbers')
    print('2. add number')
    print('3. delete number')
    print('4. purge all numbers')
    print('5. find mean')
    print('6. find mid-range value')
    print('7. find median')
    print('8. find mode')
    print()
    print('0. exit')
    print('- - - - - - - - - - - -')
    print()


# displays the contents of a list
def showList(group):
    ## group:   list, contains values
    ## output:  string, accumulator
    ## num:     number, iterator

    output = ''

    for num in group:
        if output == '':
            output += str(num)
        else:
            output += ', ' + str(num)

    print(output)


# adds a number to a list
def addNum(group):
    ## group:   list, contains values
    ## ui:      number, user input

    ui = inputNum('Number to add: ')

    if ui != None:
        group.append(ui)
        group.sort()
        print('Number added.')
    else:
        print('Invalid number!')

    return group


# removes a number from a list
def delNum(group):
    ## group:   list, contains values
    ## orig:    list, duplicate of 'list' in case of error
    ## ui:      number, user input

    orig = group
    showList(group)

    try:
        ui = inputNum('Number to delete: ')
        if ui != None:
            group.remove(ui)
            print('Number removed.')
        else:
            raise ValueError

    except ValueError:
        print('Not a valid number!')

    else:
        return orig


# purges (clears) a list
def purgeList(group):
    ## group: list, contains values

    group = [] # clears actual list, rather than pointing to a new one
    print('Purge successful.')
    return group


# returns the mean of a list
def getMean(group):
    ## group:   list, contains values
    ## output:  accumulator, holds result
    ## num:     number, iterator

    output = 0

    try:
        for num in group:
            output += num

        output /= len(group)
        return output

    except:
        return 'Cannot compute; list unsuitable'


# returns the midrange of a list
def getMidRange(group):
    ## group: list, contains values

    if group == []:
        return 'Cannot compute; list invalid'

    return (min(group) + max(group)) / 2


# returns the median of a list
def getMedian(group):
    ## group:   list, contains values
    ## val1:    number, first median value
    ## val2:    number, second median value
    try:
        if (len(group) - 1) % 2 == 0:
            return group[(len(group)-1)//2]

        else:
            val1 = group[len(group)//2 - 1]
            val2 = group[len(group)//2]
            return (val1 + val2)/2

    except IndexError:
        return 'Cannot compute; list invalid'


# returns the mode(s) of a list
def getMode(group):
    ## group:   list, contains values
    ## modes:   list, accumulates modes for output
    ## counts:  dictionary, holds the count for each list value
    ## i, j:    numbers, iterators

    if group == []:
        return ['Cannot compute; list invalid']

    modes = []
    counts = {}

    for i in group:
        counts[i] = group.count(i)

    for j in counts.keys():
        if counts[j] == max(counts.values()) and j not in modes:
            modes.append(j)

    return modes


# gets number from user
def inputNum(prompt):
    ## prompt: string, countains user input prompt

    try:
        return eval(input(prompt))
    except:
        return None


main() # I wonder what happens if you comment this out?