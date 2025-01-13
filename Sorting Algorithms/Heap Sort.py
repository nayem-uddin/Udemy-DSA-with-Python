import random as rd

# we need a helper function to heapify the array
def heapify(givenlist,n,i):
  '''
  params:
  givenlist: the list to be sorted
  n: length of the list
  i: first index to start
  '''
  smallest=i
  l=2*i+1 # left child index
  r=2*i+2 # right child index
  if l<n and givenlist[l]<givenlist[smallest]:
    smallest=l
  if r<n and givenlist[r]<givenlist[smallest]:
    smallest=r
  if smallest!=i:
    givenlist[i],givenlist[smallest]=givenlist[smallest],givenlist[i]
    heapify(givenlist,n,smallest)

def heapsort(givenlist):
  n=len(givenlist)
  # building the heap
  for i in range(n//2-1,-1,-1):
    heapify(givenlist,n,i)
  for i in range(n-1,0,-1):
    givenlist[0],givenlist[i]=givenlist[i],givenlist[0]
    heapify(givenlist,i,0)
  return givenlist[::-1]

array=list(range(11))
rd.shuffle(array)
print("Original array: ",array)
print("Sorted array: ",heapsort(array))