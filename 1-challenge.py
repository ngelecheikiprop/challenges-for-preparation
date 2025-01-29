def FirstFactorial(num):
  num = int(num)
  if num == 1:
    return 1
  return FirstFactorial(num - 1) * num

# keep this function call here 
print(FirstFactorial(input()))
