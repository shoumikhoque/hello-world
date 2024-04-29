from Node import Node
from BinarySearchTree import BinarySearchTree


def find_kth_max(root, k):
    if k < 1:
        return None
    node = find_kth_max_recursive(root, k)  # get the node at kth position
    if(node is not None):  # check if node received
        return node.val  # return kth node value
    return None  # return None if no node found


counter = 0  # global count variable
current_max = None

def find_kth_max_recursive(root, k):
    global counter  # use global counter to track k
    global current_max # track current max
    if(root is None):  # check if root exists
        return None

    # recurse to right for max node
    node = find_kth_max_recursive(root.rightChild, k)
    if(counter is not k) and (root.val is not current_max):
        # Increment counter if kth element is not found
        counter += 1
        current_max = root.val
        node = root
    elif current_max == None:
        # Increment counter if kth element is not found
        # and there is no current_max set
        counter += 1
        current_max = root.val
        node = root
    # Base condition reached as kth largest is found
    if(counter == k):
        return node  # return kth node
    else:
        # Traverse left child if kth element is not reached
        # traverse left tree for kth node
        return find_kth_max_recursive(root.leftChild, k)



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
    print(find_kth_max(BST.root, 4))
