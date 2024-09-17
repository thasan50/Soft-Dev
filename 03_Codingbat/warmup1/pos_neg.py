# Tanzeem Hasan
# Belugas
# SoftDev
# K02 -- Reviewing python
# 2024-09-11
# time spent: 3 minutes
def pos_neg(a, b, negative):
  if(negative):
    return a <0 and b <0
  else:
    return (a > 0 and b < 0) or (a < 0 and b > 0)
