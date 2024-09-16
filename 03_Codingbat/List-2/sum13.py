def sum13(nums):
  sum = 0
  for i in range(len(nums)):
    print(i)
    if nums[i] == 13:
      print("This is the other case")
      i += 1
    else:
      sum += nums[i]
  return sum
#print(sum13([1, 2, 2, 1]))
print(sum13([1, 2, 13, 2, 1, 13]))
