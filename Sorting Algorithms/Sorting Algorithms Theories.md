### **Bubble Sort**

- Keep swapping each two adjacent elements, when the previous one is greater than the next one, until the whole array is sorted

### **Selection Sort**

- Keep moving from left to right
- Keep finding out the index of the minimum element among the values less than the current element available in the rest of the array and swap it with the element of the current position

### **Insertion Sort**

- After each iteration, it is ensured that the array is sorted up to the current position

### **Bucket Sort**

- Create buckets and distribute elements of the array into the buckets
- Sort the buckets individually
- Merge the buckets after sorting

### **Merge Sort**

- Divide-and-conquer algorithm
- Divide the array into halves recursively until no more division is possible
- Merge halves by sorting them

### **Quick Sort**

- A divide and conquer algorithm
- Partitions the list into two sublists based on pivot elements.
- One sublist is arranged to contain the elements less than the pivot, and the other is arranged to contain the elements greater than the pivot.
- The above steps are performed until the whole sublist (and the original list as a result) is completely sorted. Usually, the rightmost element is considered the pivot.

### **Heap Sort**

- Insert the data to a binary heap tree
- Extract the data from the binary heap tree and insert them to the original array
