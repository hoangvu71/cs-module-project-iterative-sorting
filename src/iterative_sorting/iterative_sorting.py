# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for unsorted_index in range(i, len(arr)):
            if arr[unsorted_index] < arr[smallest_index]:
                smallest_index = unsorted_index
        # TO-DO: swap
        arr.insert(cur_index, arr[smallest_index])
        arr.insert(smallest_index + 1, arr[cur_index + 1])
        arr.pop(cur_index + 1)
        arr.pop(smallest_index + 1)
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    unsorted = True
    
    # While the list is not sorted
    while unsorted:

      # keep track if they are sorted
      count = 0

      # Loop through the array
      for i in range(1, len(arr)):
          prev =i - 1
          current = i

          # if the current value is less than the previous value
          if arr[current] < arr[prev]:

              # switch their places
              arr.insert(prev, arr[current])

              arr.insert(current+1, arr[prev + 1])

              arr.pop(current + 2)

              arr.pop(current + 1)
              
              # keep track if they are sorted
              count -= 1

      # if count is still the same value ( 0 ), then it means
      # all value in array is sorted
      # make unsorted becomes False
      if count == 0:
        unsorted = False
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
