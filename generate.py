from random import random,randint
import pickle as pk
import numpy as np
        
def returnRandomGrid(size):
    grid=[]
    In=[0]*(size*size)
    for i in range(size):
        here=[]
        for j in range(size):
            a=int(random()*size*size)
            while In[a]:
                a=int(random()*size*size)
            here.append(a)
            In[a]=1
        grid.append(here)
    a=0;b=0
    for i in range(size):
        for j in range(size):
            grid[i][j]+=1
            if grid[i][j]==size*size:
                a=i;b=j
    return grid
             
def checkWin(grid):
    v=1
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]!=v:
                return False
    return True

def printGrid(grid):
    print()
    for i in grid:
        print(i)
    print()
def inversion(arr):
    count=0
    for i in range(15):
        for j in range(16):
            if arr[i]!=16 and arr[j]!=16 and arr[i]>arr[j]:
                count+=1
    return count
def find(grid,value):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==value:
                return i
    return False
def isSolvable(grid):
    invcount=inversion(np.reshape(grid,16))
    pos=find(grid,16)
    if pos&1:
        return not (invcount&1)
    else:
        return invcount&1
def calculateNumberOfWellPlaceTiles(grid):
    count=0
    ans=0
    for i in range(len(grid)):
        for j in range(len(grid)):
            count+=1
            if grid[i][j]==count:
                ans+=1
    return ans

def distance(a,b,x,y):
    return (abs(a-x)**2 +abs(b-y)**2)**0.5

def calculateClosestnessOfTile(grid):
    sixteen=find(grid,16)
    count=0
    ans=0
    for i in range(len(grid)):
        for j in range(len(grid)):
            count+=1
            gridvalue=grid[i][j]
            x,y=gridvalue//4,gridvalue%4
            ans+=distance(i+1,j+1,x,y)
    return ans



def getBatch(size=100):
    result=[]
    for i in range(size):
        g=returnRandomGrid(4)
        r=isSolvable(g)
        if r:
            result.append([calculateNumberOfWellPlaceTiles(g),calculateClosestnessOfTile(g)])
    return np.asarray(result)


