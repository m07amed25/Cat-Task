def max_bishop_sum(test_cases):
    results = []
    for case in test_cases:
        n, m, grid = case
        max_sum = 0

        for i in range(n):
            for j in range(m):
                current_sum = 0
                x, y = i, j
                
                # Add cells in main diagonal
                while x >= 0 and y >= 0:
                    current_sum += grid[x][y]
                    x -= 1
                    y -= 1
                x, y = i + 1, j + 1
                while x < n and y < m:
                    current_sum += grid[x][y]
                    x += 1
                    y += 1

                # Add cells in the anti-diagonal
                x, y = i, j
                while x >= 0 and y < m:
                    current_sum += grid[x][y]
                    x -= 1
                    y += 1
                x, y = i + 1, j - 1
                while x < n and y >= 0:
                    current_sum += grid[x][y]
                    x += 1
                    y -= 1

                # The cell added twice
                if n > 1 or m > 1:
                    current_sum -= grid[i][j]
                
                max_sum = max(max_sum, current_sum)
        
        results.append(max_sum)
    return results


t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, m, grid))

results = max_bishop_sum(test_cases)
for res in results:
    print(res)
