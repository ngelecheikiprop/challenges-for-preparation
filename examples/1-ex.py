def str1instr2(str1, str2):
  for c in str1:
    if not (str1.count(c) <= str2.count(c)):
      return 0
  return 1

if str1instr2('chem', 'kiprop'):
  print('found you')
else:
  print('ooo no')