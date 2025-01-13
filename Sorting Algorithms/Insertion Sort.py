import random as rd

def insertionSort(givenlist):
  for i in range(1, len(givenlist)):
    key = givenlist[i]
    j = i-1
    while j>=0 and givenlist[j] > key:
      givenlist[j+1] = givenlist[j]
      j -= 1
    givenlist[j+1] = key
  return givenlist

array= list(range(11))
rd.shuffle(array)
print("Original array: ",array)
print("Sorted array: ",insertionSort(array))