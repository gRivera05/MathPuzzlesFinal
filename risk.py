from fractions import Fraction

from functools import lru_cache

#the number after the A represents the number of Attackes, and the number after the D represents the number of Defenders
#The variables with only a single fraction represent the scenatios where teh attackers can only win or lose
#the lists are for those scenarios where attackers can either beat both defenders, or only one
#to see how these values were calculated, check the slide show

A1D1 = Fraction(15, 36) 
A1D2 = Fraction(55, 216)
A2D1 = Fraction(125, 216)
A2D2 = [Fraction(295, 1296), Fraction(420, 1296)] 
A3D1 = Fraction(855, 1296)
A3D2 = [Fraction(2890, 7776), Fraction(2611, 7776)]

@lru_cache(maxsize=None) #This is simply a time optimization that stores the results of previous calls of battle(i, i) for calculations in memory
def battle(a, d): #This is a recursive fuction that essentially does a tree search to find the odds that the attacker wins considering an all out attack
    if(a>=3):
        if(d>=2):
            return (A3D2[0] * battle(a, d-2)) + (A3D2[1] * battle(a-1, d-1)) + ((1-sum(A3D2)) * battle(a-2, d))
        elif(d == 1):
            return (A3D1) + ((1-A3D1) * battle(a-1, d))
        else:
            return 1
    elif(a==2):
        if(d>=2):
            return(A2D2[0] * battle(a, d-2)) + (A2D2[1] * battle(a-1, d-1))
        elif(d == 1):
            return(A2D1) + ((1-A2D1) * battle(a-1, d))
        else:
            return 1
    elif (a==1):
        if(d>=2):
            return(A1D2 * battle(a, d-1))
        elif(d == 1):
            return(A1D1 * battle(a, d-1))
        else:
            return 1
    else:
        return 0

