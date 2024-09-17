# Tanzeem Hasan
# Belugas
# SoftDev
# K02 -- Reviewing python
# 2024-09-11
# time spent: 3 minutes
def sum67(nums):
  blocked = False
  switch = False
  sum = 0
  for i in range(len(nums)):
    if nums[i] == 6:
      blocked = True
    elif nums[i] == 7:
      switch = True

    if not blocked:
      sum += nums[i]
    if switch:
      blocked = False
      switch = False
  return sum
