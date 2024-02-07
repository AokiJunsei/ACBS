N = int(input())
score_list = [int(x) for x in (input().split())]

Alice_point = 0
Bob_point = 0

while len(score_list) > 0:
    Alice_point += max(score_list)
    score_list.remove(max(score_list))
    if len(score_list) > 0:
        Bob_point += max(score_list)
        score_list.remove(max(score_list))

print(Alice_point - Bob_point)