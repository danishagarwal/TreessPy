class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right= rightTree
    return root

def leafNode(root):
    if root.left == None and root.right == None:
        return 1
    if root == None:
        return 0
    leafLeft = leafNode(root.left)
    leafRight = leafNode(root.right)
    return leafLeft + leafRight

    
