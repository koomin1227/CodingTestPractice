from sys import stdin
input = stdin.readline



def make_tree(tree,new_ino):
    if len(new_ino) == 1:
        return new_ino[0][0]
    root = -1
    root_pri = 10000
    for i in range(len(new_ino)):
        if root_pri > new_ino[i][1]:
            root_pri = new_ino[i][1]
            root = i
    if root>0:
        tree[new_ino[root][0]][0] = make_tree(tree, new_ino[:root])
    if root<len(new_ino)-1:
        tree[new_ino[root][0]][1] = make_tree(tree, new_ino[root+1:])
    return new_ino[root][0]

def post_order(node,tree):
    if tree[node][0] != 0:
        post_order(tree[node][0], tree)
    if tree[node][1] != 0:
        post_order(tree[node][1], tree)
    print(node,end=' ')

t = int(input())
for _ in range(t):
    n = int(input())
    pre = list(map(int,input().split()))
    ino = list(map(int,input().split()))
    if n == 1:
        print(pre[0])
    else:
        new_ino = []
        for i in ino:
            new_ino.append([i,pre.index(i)])
        tree = [[0,0]for i in range(n+1)]
        root = ino.index(pre[0])
        if root>0:
            tree[pre[0]][0] = make_tree(tree,new_ino[:root])
        if root<len(new_ino)-1:
            tree[pre[0]][1] = make_tree(tree,new_ino[root+1:])
        post_order(pre[0],tree)
        print()


