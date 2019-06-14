#!/usr/bin/env python3
# Find a deepest tree node.
# Mario Stanke, August 23rd, 2018

sons = {} # keys: nodes, values: lists of sons
treefile = open("taxonomy.tree", "r")
root = 1
for line in treefile:
    x, y = line.strip().split('\t')
    x = int(x)
    y = int(y)
    if (y not in sons):
        sons[y] = []
    if (x != root):
        sons[y].append(x)
    
treefile.close()

maxdepth = 0
deepestnode = root

def dfs(u, depth):
    global maxdepth, deepestnode
    if (depth > maxdepth):
        maxdepth = depth
        deepestnode = u
    if (u in sons):
        for v in sons[u]:
            dfs(v, depth+1)

dfs(root, 0)
print ("Node", deepestnode, "has maximal depth", maxdepth)
