# Tanzeem Hasan
# Belugas
# SoftDev
# K02 -- Reviewing python
# 2024-09-11
# time spent: 3 minutes
def front_back(str):
  if len(str) < 2:
    return str
  return str[len(str) - 1] + str[1:len(str)-1] + str[0]
