from concept.DataStructure.BST.BinarySearchTree import BinarySearchTree


def findHeight(root,h=0):
    if root is None:
        return h
    return 1+max(findHeight(root.leftChild,h),findHeight(root.rightChild,h))



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

    # BST.insert(21)
    # BST.insert(29)
    # BST.insert(31)
    # BST.insert(39)

    print(findHeight(BST.root,0))