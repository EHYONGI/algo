# teacher

def solution(my_string, letter):
    answer = ''

    answer = my_string.replace(letter, '')

    return answer

print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))