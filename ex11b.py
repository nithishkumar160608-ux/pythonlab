from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    traversal = []

    while queue:
        user = queue.popleft()
        traversal.append(user)

        for friend in graph[user]:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)

    return traversal



def dfs(graph, start):
    visited = set()
    stack = [start]

    traversal = []

    while stack:
        user = stack.pop()

        if user not in visited:
            visited.add(user)
            traversal.append(user)

       
            for friend in reversed(graph[user]):
                if friend not in visited:
                    stack.append(friend)

    return traversal



n = int(input("Enter no. of users: "))


graph = {i: [] for i in range(n + 1)}


m = int(input("Enter no. of friendships: "))

print("Enter the friendships:")

for i in range(m):
    u, v = map(int, input().split())


    graph[u].append(v)
    graph[v].append(u)



for user in graph:
    graph[user].sort()


print("\nSocial Network:")

for user in graph:
    print(user, "->", graph[user])



friend_user = int(input("\nEnter user to find friends: "))

if friend_user in graph:
    print("Friends of user", friend_user, ":", graph[friend_user])
else:
    print("User not found.")
   
start = int(input("Enter starting user for BFS and DFS: "))

if start not in graph:
    print("Invalid starting user.")
else:
   
    bfs_result = bfs(graph, start)

    print("\nBFS Traversal:")
    print(" ".join(map(str, bfs_result)))


    dfs_result = dfs(graph, start)

    print("\nDFS Traversal:")
    print(" ".join(map(str, dfs_result)))
