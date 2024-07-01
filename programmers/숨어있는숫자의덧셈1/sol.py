def solution(my_string):
    answer = 0
    one = '123456789'
    
    for char in my_string:
        if char in one:
            answer += int(char)
    
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))