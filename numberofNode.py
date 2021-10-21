'''time complexity O(n) --> N is the number of nodes. 
Basically n * Constant time --> O(n)'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def numNodes(root):
    if root == None:
        return 0
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    return 1 + leftCount + rightCount


def printTreeDetails(root):
    if root == None:
        return

    print(root.data, end = " : ")
    if root.left != None:
        print("L ", root.left.data, end = ',')
    if root.right != None: 
        print("R ", root.right.data, end = " ")
    print()
    printTreeDetails(root.left)   
    printTreeDetails(root.right)
    
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

root = treeInput()

printTreeDetails(root)
print(numNodes(root))
