# if element is found, return the index, otherwise return -1
def linearsearch(array,value):
  for i in range(len(array)):
    if array[i]==value:
      return i
  return -1

print(linearsearch([1,2,4,3],0))
print(linearsearch([1,2,4,3],3))