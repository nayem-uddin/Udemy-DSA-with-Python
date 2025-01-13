import random as rd

# here, partition is a helper function to place the pivot to the correct position, and sort the elements at its left and right
def partition(givenlist,low,high):
  '''
  params:
  givenlist: the list to be sorted
  low: first index of the list
  high: last index of the list
  '''
  i=low-1
  pivot=givenlist[high]
  for j in range(low,high):
    if givenlist[j]<=pivot:
      i+=1
      givenlist[i],givenlist[j]=givenlist[j],givenlist[i] # less elements should be kept at the left
  givenlist[i+1],givenlist[high]=givenlist[high],givenlist[i+1] # placing the pivot to the correct position
  return i+1

def quicksort(givenlist,low,high):
  if low<high:
    pi=partition(givenlist,low,high) # the updated index of the pivot
    quicksort(givenlist,low,pi-1)
    quicksort(givenlist,pi+1,high)
  return givenlist

array=list(range(11))
rd.shuffle(array)
print("Original array: ",array)
print("Sorted array: ",quicksort(array,0,len(array)-1))