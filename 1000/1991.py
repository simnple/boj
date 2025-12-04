preorder = []
inorder = []
postorder = []

def dfs(node):
    if node == ".": return

    preorder.append(node)
    for is_right in range(2):
        child = graph[node][is_right]

        if is_right == 1: inorder.append(node)

        dfs(child)

    postorder.append(node)

graph = dict()

N = int(input())

for _ in range(N):
    parent, left_child, right_child = input().split()
    graph[parent] = [left_child, right_child]

dfs("A")

print("".join(preorder))
print("".join(inorder))
print("".join(postorder))