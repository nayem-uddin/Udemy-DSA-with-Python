def binarysearch(array, value):
  start = 0 # pointer at the beginning
  end = len(array)-1 # pointer at the end
  middle = (start+end)//2 # pointer at the middle
  while not array[middle]==value and start<=end:
    if value<array[middle]:
      end = middle-1
    else:
      start = middle+1
    middle = (start+end)//2
  if array[middle]==value:
    return middle
  return -1

print(binarysearch([1,2,3,4],0))
print(binarysearch([1,2,3,4],3))