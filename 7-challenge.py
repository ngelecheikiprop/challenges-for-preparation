#!/usr/bin/python3
def TreeConstructor(strArr):
  for i in range(10):
    child_count = 0
    for item in strArr:
      if str(i) == item.split(',')[1][:-1]:
        child_count += 1
    if child_count > 2:
      return 'false'
  for i in range(10):
    parent_count = 0
    for item in strArr:
      if str(i) == item.split(',')[0][1:]:
        parent_count += 1
    if parent_count > 1:
      return 'false'
  return 'true'


print(TreeConstructor(input()))
