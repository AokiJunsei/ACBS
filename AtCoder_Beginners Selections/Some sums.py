N, A, B = map(int, input().split())

answer = 0

for i in range(N + 1):
    total = sum(int(j) for j in list(str(i)))
    
    if A <= total and B >= total:
        answer += i

print(answer)



