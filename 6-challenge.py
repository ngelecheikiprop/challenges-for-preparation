#!/usr/bin/python3 

def BracketMatcher(strParam):
    j = -1
    for i in range(len(strParam)):
        if strParam[i] == '(':
            for i in range(len(strParam)):
                while strParam[j] != ')':
                    if i > len(strParam) + j:
                        return 0
                    j -= 1
        elif i == len(strParam) - 1:
            return 0
    return 1
print(BracketMatcher(input()))
