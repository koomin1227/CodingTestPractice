from sys import stdin
input = stdin.readline

def traverse(tree: dict, depth):
    keys = list(tree.keys())
    keys.sort()
    for key in keys:
        print('--'*depth + key)
        traverse(tree[key], depth + 1)

n = int(input())
tree = {}

for _ in range(n):
    info = list(map(str, input().split()))
    info.pop(0)
    node = tree
    for i in range(len(info)):
        if info[i] not in node:
            node[info[i]] = {}
        node = node[info[i]]

traverse(tree, 0)