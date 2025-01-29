#!/usr/bin/python3
def TreeConstructor(strArr):
  for i in range(10):
    count = 0
    for item in strArr:
      if str(i) in item.split(',')[1]:
        count += 1
    if count > 2:
      return 'false'
  return 'true'

print(TreeConstructor(input()))
