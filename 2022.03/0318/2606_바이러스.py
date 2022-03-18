n = int(input())
m = int(input())

graph = [[]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def find(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            find(i)

find(1)
for b in visited:
    if b == True:
        cnt += 1
print(cnt - 1)