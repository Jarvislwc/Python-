# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        '''
        二元樹:In-Order排序
        Left -> Root -> Right
        先找左邊 往下探勘
        如果有就繼續往下 直到沒有
        然後拜訪
        在往上拜訪
        先開一個陣列存取
        用Recursive寫
        看資結筆記
        '''
        a = []
        self.inorder(root, a)
        return a

    def inorder(self, root, a) -> None:
        if root == None:
            return
        self.inorder(root.left, a)
        a.append(root.val)
        self.inorder(root.right, a)
