## 수학적 접근

def solution(n):
    answer = 0

# 10으로 나눴을 때 나머지가 각 자릿수 !

    while n > 0:
        # a에는 몫, b에는 나머지
        a, b = divmod(n, 10)

        n = a
        answer += b

    return answer

print(solution(1234))
print(solution(930211))