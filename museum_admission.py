# 'Ze Primary Computational Function
def computeAdmission(numChilds, numAdults, numSeniors):
    price = 0;
    price += numAdults * 7
    price += numSeniors * 55
    if (numChilds < 4):
        price += numChilds * 4
    else:
        price += numChilds * 3.5
    return price


# or, to put it much more compactly (easy to read, no?) ...

#   def computeAdmission(numChilds, numAdults, numSeniors):
#       return (numAdults*7)+(numSeniors*5)+(numChilds*4 if (numChilds<4) else numChilds*3.5)


# helper function
def inputInt(prompt):
    return int(input(prompt))

## --- MAIN --- ##

# input
children = inputInt("Enter the number of children: ")
adults = inputInt("Enter the number of adults: ")
seniors = inputInt("Enter the number of seniors: ")

# just finding the correct word forms (singular/plural)
cText = " child, " if (children == 1) else " children, "
aText = " adult, " if (adults == 1) else " adults, "
sText = " senior, " if (seniors == 1) else " seniors, "

# compute the total amount
total = computeAdmission(children, adults, seniors)

# output
print()
print(children, cText, adults, aText, seniors, sText, ' ...', sep='')
print('That will be $', total, ', please.', sep='')
