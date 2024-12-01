class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def search_bst(root: TreeNode, val: int) -> TreeNode:
    if root is None or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)

def insert_into_bst(root: TreeNode, val: int) -> TreeNode:
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def inorder_traversal(root: TreeNode):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

if __name__ == "__main__":
    root = None
    values = [4, 2, 7, 1, 3]
    for val in values:
        root = insert_into_bst(root, val)
    # inorder_traversal(root)
    target = 2
    result = search_bst(root, target)
    if result:

        inorder_traversal(result)
        print("\n")
    else:
        print(f"Value {target} not found in the BST.")

