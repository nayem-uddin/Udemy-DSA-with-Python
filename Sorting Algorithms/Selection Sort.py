import random as rd

def selectionsort(givenlist):
  for i in range(len(givenlist)):
    min_index=i
    for j in range(i+1,len(givenlist)):
      if givenlist[min_index]>givenlist[j]:
        min_index=j
    givenlist[i],givenlist[min_index]=givenlist[min_index],givenlist[i]
  return givenlist

array= list(range(11))
rd.shuffle(array)
print("Original array: ",array)
print("Sorted array: ",selectionsort(array))