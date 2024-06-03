from concept.BST.BinarySearchTree import BinarySearchTree

ancestorList=[]
def findAncestors(root, k):
    global ancestorList
    if root is None:
        return None
    if root.val==k:
        return ancestorList
    if root.val<k:
        ancestorList.append(root.val)
        findAncestors(root.rightChild,k)
    else:
        ancestorList.append(root.val)
        findAncestors(root.leftChild, k)


if __name__ == '__main__':
    BST = BinarySearchTree(20)
    BST.insert(10)
    BST.insert(30)
    BST.insert(5)
    BST.insert(15)
    BST.insert(25)
    BST.insert(35)
    BST.insert(1)
    BST.insert(9)
    BST.insert(11)
    BST.insert(19)

    BST.insert(21)
    BST.insert(29)
    BST.insert(31)
    BST.insert(39)
    findAncestors(BST.root, 21)
    print(ancestorList)