def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for word in words:
            babbling[i] = babbling[i].replace(word, ' ')
        babbling[i] = babbling[i].replace(' ', '')
    return babbling.count('')

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))

# 문자열 해당 문자 포함할 경우 공백으로 대치해서 재귀 후 빈문자열 가진 배열만 세기 !