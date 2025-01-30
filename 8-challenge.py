def str1instr2(str1, str2):
  for c in str1:
    if not (str1.count(c) <= str2.count(c)):
      return 0
  return 1

def MinWindowSubstring(strArr):
    stringN = strArr[0]
    stringK = strArr[1]
    subString = ''
    i = 0
    while i < len(stringN) - 1:
        if str1instr2(stringK, stringN[i+1:]):
            subString =  stringN[i+1:]
        i += 1

    newStringN = subString[::-1]
    subString = ''
    i= 0
    while i < len(newStringN) - 1:
        if str1instr2(stringK, newStringN[i+1:]):
            subString =  newStringN[i+1:]
        i += 1
    
    return subString[::-1]

print(MinWindowSubstring(["aaaaaaaaa", "a"]))