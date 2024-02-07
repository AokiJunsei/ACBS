def counter(nums):
    count = 0
    while all(num % 2 == 0 for num in nums):
        count += 1
        nums = [num // 2 for num in nums]
    return count


n = int(input())
A = [int(x) for x in (input().split())]
print(counter(A))