# Tanzeem Hasan
# Belugas
# SoftDev
# K02 -- Reviewing python
# 2024-09-11
# time spent: 3 minutes
def max_end3(nums):
  num = 0

  if nums[0] > nums[-1]:
    num = nums[0]
  else:
    num = nums[-1]

  for i in range(len(nums)):
    nums[i] = num
  return nums
