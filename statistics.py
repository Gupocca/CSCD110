import math

def main():
    lst = []

    showMenu()
    cmd = inputNum('Enter Command: ')

    while (cmd != 0):
        if cmd == 1:
            showList(lst)
        
        elif cmd == 2:
            lst = addNum(lst)
        
        elif cmd == 3:
            lst = delNum(lst)
        
        elif cmd == 4:
            lst = purgeList(lst)
        
        elif cmd == 5:
            print(getMean(lst))
        
        elif cmd == 6:
            print(getMidRange(lst))
        
        elif cmd == 7:
            print(getMedian(lst))
        
        elif cmd == 8:
            print(getMode(lst))
        
        else:
            print('Invalid command!')
        
        showMenu()
        cmd = inputNum('Enter Command: ')
    

def showMenu():
    print()
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
    print()

def showList(group):
    print()
    output = ''
    for num in group:
        if (output == ''):
            output += str(num)
        else:
            output += ', ' + str(num)
    print(output)

def addNum(group):
    ui = inputNum('Number to add: ')
    group.append(ui)
    group.sort()
    return group

def delNum(group):
    showList(group)
    print()

    ui = inputNum('Number to delete: ')
    group.remove(ui)
    group.sort()
    return group

def purgeList(group):
    for i in group:
        group.pop(i)

    return group

def getMean(group):
    output = 0;

    for num in group:
        output += num
    
    output /= len(group)
    return output

def getMidRange(group):
    pass

def getMedian(group):
    if (len(group) - 1 % 2):
        return group[(len(group)-1)//2]
    else:
        ind = math.floor((len(group)-1) / 2)
        val1 = group[ind]
        val2 = group[ind + 1]
        return (val1 + val2)/2

def getMode(group):
    pass

def inputNum(prompt):
    # should have validation eventually
    return int(input(prompt))
    
main()
