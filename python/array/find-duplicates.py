def find_duplicates(arr1, arr2):
      duplicates = []
  for number in arr1:
    if binary_search(arr2, number) != -1:
      duplicates.append(number)
  return duplicates

def binary_search(arr, num):
  begin = 0
  end = len(arr) - 1
  
  while (begin <= end):
    mid = begin + ((end - begin)//2)
    if arr[mid] < num:
      begin = mid + 1
    elif arr[mid] == num:
      return mid
    else:
      end = mid - 1
  return -1