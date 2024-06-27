def solution(n, k):

    answer = n * 12000 + k * 2000 - ((n//10) * 2000)
    return answer

print(solution(10, 3))
print(solution(64, 6))

# teacher

def solution(n, k):

    answer = 0

    food_price = n * 12000

    if n >= 10:
        serve = n // 10
        drink_price = (k - serve) * 2000
    else:
        drink_price = k * 2000

    return food_price + drink_price

print(solution(10, 3))
print(solution(64, 6))