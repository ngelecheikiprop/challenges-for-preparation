def FirstReverse(strParam):
  reversed_string = ""
  str_length = len(strParam)
  for i in range(1,str_length + 1 ):
    reversed_string += strParam[-i]

  return reversed_string

print(FirstReverse(input()))
