import sys

N = int(input())
data = [[] for _ in range(N+1)]
visited = [False] * (N+1)
maxdis = []
while True:
    try:
        index, next, dis = map(int, sys.stdin.readline().strip().split())
        data[index].append([next,dis])
    except:
        break

def dfs(root, dis):
    if not data[root] :
        return dis
    visited[root] = True
    node_list = []
    for i in data[root] :
        if not visited[i[0]] :
            val = dfs(i[0], i[1])
            node_list.append(val)
    maxdis.append(sum(node_list))
    return max(node_list) + dis

dfs(1, 0)     
# print(data)
# print(visited)
print(max(maxdis))