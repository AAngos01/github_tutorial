
import math

def median(input):
  input.sort()
  if len(input) % 2 == 0:
    return (input[math.floor(len(input) / 2)] + input[math.floor(len(input) / 2) - 1]) / 2
  else:
    return input[math.floor(len(input) / 2)]

def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)

print("hello_world")
