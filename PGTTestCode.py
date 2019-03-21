import numpy as np
import copy as cp
import random


##### Factors #####
#The various factors that account for the payoffs of each actor.

# God's Favor
#A truthful belief in god is rewarded greatly
Favor = 3

# God's Disfavor
#God punishes heathens greatly
Disfavor = -3

# Agreement
#Those in agreement are happier
Agreement = 2

# Disagreement
#Those in disagreement are unhappier
Disagreement = -2

# Skepticism
#A successful nonbelief in God's existence is accurate
Skepticism = 2

# Delusion
#Fallacious faith in God is an inconvenient belief
Delusion = -2

#Anti god punishes belief
aBelief = -4

#Anti god likes non belief (but doesnt care that much cause they r evil)
aNonBelief = 1

# BaseMatrix
#An array of 2 2darrays that each represent
#the payoff matrix for group 1 and group 2 respectively.
BaseMatrix = np.zeros((2, 2, 2))

#Matrix Creation
def yesGod(matrix):
    newMatrix = cp.copy(matrix)
    #Player 1:
    for i in [newMatrix[0][0, :]]:
        i += Favor
    for i in [newMatrix[0][1, :]]:
        i += Disfavor

    newMatrix[0][0, 0] += Agreement
    newMatrix[0][1, 0] += Disagreement
    newMatrix[0][0,1] += Disagreement
    newMatrix[0][1,1] += Agreement
        
    #Player 2:
    newMatrix[1][0, 0] += Favor
    newMatrix[1][1, 0] += Favor
    newMatrix[1][0,1] += Disfavor
    newMatrix[1][1,1] += Disfavor

    newMatrix[1][0, 0] += Agreement
    newMatrix[1][1, 0] += Disagreement
    newMatrix[1][0,1] += Disagreement
    newMatrix[1][1,1] += Agreement

    return newMatrix

def noGod(matrix):
    newMatrix = cp.copy(matrix)
    #Player 1:
    for i in [newMatrix[0][0, :]]:
        i += Delusion
    for i in [newMatrix[0][1, :]]:
        i += Skepticism

    newMatrix[0][0, 0] += Agreement
    newMatrix[0][1, 0] += Disagreement
    newMatrix[0][0,1] += Disagreement
    newMatrix[0][1,1] += Agreement
        
    #Player 2:
    newMatrix[1][0, 0] += Delusion
    newMatrix[1][1, 0] += Delusion
    newMatrix[1][0,1] += Skepticism
    newMatrix[1][1,1] += Skepticism

    newMatrix[1][0, 0] += Agreement
    newMatrix[1][1, 0] += Disagreement
    newMatrix[1][0,1] += Disagreement
    newMatrix[1][1,1] += Agreement

    return newMatrix

def idcGod(matrix):
    newMatrix = cp.copy(matrix)
    #Player 1:

    newMatrix[0][0, 0] += Agreement
    newMatrix[0][1, 0] += Disagreement
    newMatrix[0][0,1] += Disagreement
    newMatrix[0][1,1] += Agreement
        
    #Player 2:
    
    newMatrix[1][0, 0] += Agreement
    newMatrix[1][1, 0] += Disagreement
    newMatrix[1][0,1] += Disagreement
    newMatrix[1][1,1] += Agreement
    
    return newMatrix


def antiGod(matrix):
    newMatrix = cp.copy(matrix)
    #Player 1:
    for i in [newMatrix[0][0, :]]:
        i += aBelief
    for i in [newMatrix[0][1, :]]:
        i += aNonBelief

    newMatrix[0][0, 0] += Agreement
    newMatrix[0][1, 0] += Disagreement
    newMatrix[0][0,1] += Disagreement
    newMatrix[0][1,1] += Agreement
        
    #Player 2:
    newMatrix[1][0, 0] += aBelief
    newMatrix[1][1, 0] += aBelief
    newMatrix[1][0,1] += aNonBelief
    newMatrix[1][1,1] += aNonBelief

    newMatrix[1][0, 0] += Agreement
    newMatrix[1][1, 0] += Disagreement
    newMatrix[1][0,1] += Disagreement
    newMatrix[1][1,1] += Agreement

    return newMatrix

#choose matrix functions
def chooseMatrix():
    sitch = random.randint(0,3)
    if sitch == 0:
        matrix = yesGod(BaseMatrix)
    elif sitch == 1:
        matrix = noGod(BaseMatrix)
    elif sitch == 2:
        matrix = idcGod(BaseMatrix)
    elif sitch == 3:
        matrix = antiGod(BaseMatrix)

    return matrix
    
    
#P1B & P2B
def bothBelieve():
    P1B = 0
    P2B = 0
    
    #P1B (0) P2B (0)
    for i in range(1000):
        
        matrix = chooseMatrix()
                
        P1B += matrix[0][0,0]
        P2B += matrix[1][0,0]

    return P1B, P2B

#P1B & P2D
def bothDisbelieve():
    P1B = 1
    P2B = 1
    
    #P1B (0) P2B (0)
    for i in range(1000):
        
        matrix = chooseMatrix()
                
        P1B += matrix[0][1,1]
        P2B += matrix[1][1,1]

    return P1B, P2B

#P1B & P2D
def believeDis():
    P1B = 0
    P2D = 1
    
    #P1B (0) P2B (0)
    for i in range(1000):
        
        matrix = chooseMatrix()
                
        P1B += matrix[0][0,1]
        P2D += matrix[1][0,1]

    return P1B, P2D
#P1D & P2B
def disBelieve():
    P1D = 1
    P2B = 0
    
    #P1B (0) P2B (0)
    for i in range(1000):
        
        matrix = chooseMatrix()
                
        P1D += matrix[0][1,0]
        P2B += matrix[1][1,0]

    return P1D, P2B
    
    
#Main function
def Main():

    P1B, P2B = bothBelieve()

    print("P1B = ", P1B, " & P2B = ", P2B)

    P1D, P2D = bothDisbelieve()

    print("P1D = ", P1D, " & P2D = ", P2D)

    P1B, P2D = believeDis()

    print("P1B = ", P1B, " & P2D = ", P2D)

    P1D, P2B = disBelieve()

    print("P1D = ", P1D, " & P2B = ", P2B)

    

    
Main()

