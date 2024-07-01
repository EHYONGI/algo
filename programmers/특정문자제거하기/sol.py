def solution(my_string, letter):
    answer = ''

    for l in my_string:
        if l not in letter:
            answer += l

    return answer

print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))