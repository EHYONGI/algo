def solution(my_string, letter):
    answer = ''

    for l in my_string:
        if l != letter:
            answer += l

    return answer

print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))