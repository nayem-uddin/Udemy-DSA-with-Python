import random as rd
from math import *
def bucketsort(givenlist):
  nob=isqrt(len(givenlist)) # no. of buckets
  maxvalue=max(givenlist)
  buckets=[[] for i in range(nob)] # creating buckets
  # distributing elements into buckets
  for ele in givenlist:
    bucket=ceil(ele*nob/maxvalue)
    buckets[bucket-1].append(ele)
  # sorting buckets individually
  for i in range(nob):
    buckets[i].sort()
  # merging buckets
  k=0
  for i in range(nob):
    for j in range(len(buckets[i])):
      givenlist[k]=buckets[i][j]
      k+=1
  return givenlist

array= list(range(1,11))
rd.shuffle(array)
print("Original array: ",array)
print("Sorted array: ",bucketsort(array))