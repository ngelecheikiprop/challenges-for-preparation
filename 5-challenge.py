def QuestionsMarks(strParam):
  found_flag = ''
  numbers_index_list = findNumbersIndex(strParam)
  for i in range(len(numbers_index_list) - 1):
    if int(strParam[numbers_index_list[i]]) + int(strParam[numbers_index_list[i + 1]]) == 10:
      if strParam[numbers_index_list[i] : numbers_index_list[i + 1]].count('?') == 3:
        found_flag += '1'
      else:
        found_flag += '0'
  if '0' in found_flag:
      return 'false'
  else:
      return 'true'

def findNumbersIndex(strParam):
  numbers_index_list = []
  for i in range(len(strParam)):
    if strParam[i].isdigit():
      numbers_index_list.append(i)
  return numbers_index_list

print(QuestionsMarks(input()))
