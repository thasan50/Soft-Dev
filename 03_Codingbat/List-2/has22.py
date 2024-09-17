# Tanzeem Hasan
# Belugas
# SoftDev
# K02 -- Reviewing python
# 2024-09-11
# time spent: 3 minutes
def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 2:
      if nums[i + 1] == 2:
        return True
  return False
