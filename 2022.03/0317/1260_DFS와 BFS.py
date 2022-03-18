from collections import deque

n, m, v = map(int, input().split())
# 간선은 양방향이다.
graph = [[] * (n+1) for _ in range(n+1)]

visited = [0] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(n):
    graph[i].sort()

def dfs(x):
    if visited[x] == 0:
        print(x, end=' ')
        visited[x] = 1
    for j in graph[x]:
        if visited[j] == 0:
            visited[j] = 1
            print(j, end=' ')
            dfs(j)

dfs(v)
print()
visited = [0] * (n+1)

def bfs(x):
    visited[x] = 1
    q = deque([x])
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

bfs(v)





