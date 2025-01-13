import random as rd

def bubblesort(givenlist):
  for i in range(len(givenlist)-1):
    for j in range(len(givenlist)-i-1):
      if givenlist[j]>givenlist[j+1]:
        givenlist[j],givenlist[j+1]=givenlist[j+1],givenlist[j]
  return givenlist

array=list(range(11))
rd.shuffle(array)
print("Original array: ",array)
print("Sorted array: ",bubblesort(array))