class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.val)

class BinaryTree:
    def __init__(self):
        self.root=None
    def insert_level_order(self, arr,root, i, n):
        if i < n and arr[i] is not None:
            temp = Node(arr[i])
            root = temp
            # Insert left child
            root.left = self.insert_level_order(arr, root.left, 2 * i + 1, n)
            # Insert right child
            root.right = self.insert_level_order(arr, root.right, 2 * i + 2, n)
        return root
    def build_tree_from_list(self,arr):
        n=len(arr)
        self.root=self.insert_level_order( arr, None, 0, n)

def rob(root:Node):
    def max_profit(root:Node):
        if not root:
            return [0,0]
        leftPair=max_profit(root.left)
        rightPair=max_profit(root.right)
        withRoot=root.val+leftPair[1]+rightPair[1]
        withoutRoot=max(leftPair)+max(rightPair)
        return [withRoot,withoutRoot]
    return max(max_profit(root))

if __name__ == '__main__':
    arr = [3,4,5,1,3,None,1]
    bt=BinaryTree()
    root = bt.build_tree_from_list(arr)
    print(rob(bt.root))
