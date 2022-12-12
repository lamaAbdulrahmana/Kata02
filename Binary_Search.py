import array
import numpy as np

def chop(target,list_object):
  array_object = np.array(list_object) # Convert list to array first
  array_object = sorted(array_object)  # Make sure array is sorted before
  lower = 0
  upper = len(array_object) - 1
  middle = 0
  while(lower <= upper): # Loop through the array to check if target exist
    middle = (lower+upper) // 2
    if(array_object[middle] == target):
      return middle # return middle value that's == to target
    else:
      if(array_object[middle] > target):  # If target is smaller change upper index
        upper = middle - 1
      else: # If target is bigger change lower index
        lower = middle + 1
      
  return -1 # return -1 if target dont exist

print(chop(45,[4,7,8,12,45,99])) # value exist
print(chop(9,[4,7,8,12,45,99])) # value dont exist