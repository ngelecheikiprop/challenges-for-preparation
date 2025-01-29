def FindIntersection(strArr):
  repeated_numbers = ''
  for number in strArr[0].split(','):
    for number2 in strArr[1].split(','):
      if number.strip() == number2.strip():
        repeated_numbers += number
        repeated_numbers += ', '
  if not repeated_numbers:
      return 'false'
  return repeated_numbers[:-2]
# keep this function call here 
print(FindIntersection(["1, 2, 3, 4, 5", ", 6, 7, 8, 9, 10"]))
