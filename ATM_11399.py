n = int(input())
work = list(map(int, input().split()))
if n == 1:
    print(work[0])
else:
    work.sort() 
    memo = {}
    result, memo[0] = work[0], work[0]
    for i in range(1, len(work)):
        memo[i] = memo[i-1] + work[i]
        result += memo[i]
    print(result)