def solve():
    N = int(input())
    coins = list(map(int, input().split()))
    
    min_coin = min(coins)
    
    dist = [float('inf')] * min_coin
    dist[0] = 0
    
    from collections import deque
    
    for coin in coins:
        if coin == min_coin:
            continue
        q = deque()
        for remainder in range(min_coin):
            if dist[remainder] != float('inf'):
                q.append(remainder)
        
        while q:
            r = q.popleft()
            next_r = (r + coin) % min_coin
            new_cost = dist[r] + coin
            
            if new_cost < dist[next_r]:
                dist[next_r] = new_cost
                q.append(next_r)
    
    answer = 0
    for r in range(min_coin):
        if dist[r] != float('inf') and dist[r] <= N - 1:
            answer += (N - 1 - dist[r]) // min_coin + 1
    
    print(answer)

solve()