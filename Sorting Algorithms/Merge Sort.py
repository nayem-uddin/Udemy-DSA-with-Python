import random as rd

# here, merge is a helper function to merge two subarrays of a custom list
def merge(customlist,l,m,r):
  '''
  params:
  customlist: the list to be sorted
  l: first index of the list
  m: middle index of the list
  r: last index of the list
  '''
  n1 = m-l+1 # the number of elements in the first subarray
  n2 = r-m # the number of elements in the second subarray
  # copying the elements of the subarrays to two distinct temporary lists
  L = [0]*n1
  R = [0]*n2
  for i in range(n1):
    L[i]=customlist[l+i]
  for j in range(n2):
    R[j]=customlist[m+1+j]
  # merging the subarrays
  i = 0
  j = 0
  k = l
  while i<n1 and j<n2:
    if L[i]<=R[j]:
      customlist[k]=L[i]
      i+=1
    else:
      customlist[k]=R[j]
      j+=1
    k+=1
  # if there are leftovers in any of the subarrays, then one of the following loops will be executed
  while i<n1:
    customlist[k]=L[i]
    i+=1
    k+=1
  while j<n2:
    customlist[k]=R[j]
    j+=1
    k+=1

def mergesort(givenlist,l,r):
  '''
  params:
  givenlist: the list to be sorted
  l: first index of the list
  r: last index of the list
  '''
  if l<r:
    m=(l+r)//2
    mergesort(givenlist,l,m)
    mergesort(givenlist,m+1,r)
    merge(givenlist,l,m,r)
  return givenlist

array= list(range(11))
rd.shuffle(array)
print("Original array: ",array)
print("Sorted array: ",mergesort(array,0,len(array)-1))