import math

def median(input):
  input.sort()
  if len(input) % 2 == 0:
    return (input[math.floor(len(input) / 2)] + input[math.floor(len(input) / 2) - 1]) / 2
  else:
    return input[math.floor(len(input) / 2)]
  
print("hello_world")
