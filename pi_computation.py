##  CSCD 110, Assignment #3
##  Stephen Hoerner 
##  Pi.

# define our function
def getPI(bound):
    result = 2  # accumulator
    i = 2       # incrementer
    
    while i <= bound:
        result *= i/(i-1) * i/(i+1) # multiply accordingly
        i += 2
        
    return result

# MAIN
upperBound = int(input('Accuracy (1 to ∞): ')) # int is preferable
print('- - - - - - - - -')
print('Pi =~', getPI(upperBound))
print('(', upperBound, ' factors; ',(upperBound + 1) // 2, ' iterations.)', sep='')