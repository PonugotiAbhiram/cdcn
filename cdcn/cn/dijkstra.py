
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:\n")
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

src = int(input("Enter source vertex: "))

dist = [float('inf')] * n
visited = [False] * n

dist[src] = 0

for i in range(n):

    u = -1
    for j in range(n):
        if not visited[j] and (u == -1 or dist[j] < dist[u]):
            u = j

    if u == -1 or dist[u] == float('inf'):
        break

    visited[u] = True

    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:
            dist[v] = min(dist[v], dist[u] + graph[u][v])

print("Shortest distances:")
for i in range(n):
    print(src, "to", i, "=", dist[i])