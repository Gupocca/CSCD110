##  CSCD 110, Assignment #3
##  Stephen Hoerner 
##  Pi.

# define our function
def getPI(bound):
    result = 2 # (1*x*2) == (2*x), so why not simplify?

    for i in range(2, bound, 2):
        # multiply accordingly
        result *= i/(i-1) * i/(i+1) 

    return result

# MAIN
upperBound = int(input('Accuracy (1 to ∞): ')) # int is preferable
print('-------------------')
print('Number of factors:', upperBound)
print('Iterations:', (upperBound + 1) // 2)
print('Pi =~', getPI(upperBound))
