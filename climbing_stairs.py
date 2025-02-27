"""
**Climbing Stairs**

You are climbing a staircase with  n  steps. Each time you can either take 1 or 2 steps. Find the number of distinct ways to reach the top.

**Example:**

Input: n = 4

Output: 5 (Ways: 1-1-1-1, 1-1-2, 1-2-1, 2-1-1, 2-2)
"""


class TreeNode:
    def __init__(self, val, left=None, right=None, sum=0, stairs=''):
        self.val = val
        self.left = left
        self.right = right
        self.sum = sum
        self.stairs = stairs


def climbing_stairs(n: int):
    tree1 = TreeNode(1, sum=1, stairs='1')
    tree2 = TreeNode(2, sum=2, stairs='2')

    fill_tree(tree1, n)
    fill_tree(tree2, n)
     


def fill_tree(tree: TreeNode, n: int):
    if tree.sum == 4:
        print(tree.stairs)
        return
    if tree.sum + 1 <= n:
        new_node = TreeNode(1)
        tree.left = new_node
        tree.left.sum = tree.sum + 1
        tree.left.stairs = tree.stairs + '-1'
        fill_tree(new_node, n)
    if tree.sum + 2 <= n:
        new_node = TreeNode(2)
        tree.right = new_node
        tree.right.sum  = tree.sum + 2
        tree.right.stairs = tree.stairs + '-2'
        fill_tree(new_node, n)

    return tree
    


if __name__ == "__main__":
    climbing_stairs(4)
    
    

            