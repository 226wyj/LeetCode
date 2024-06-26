# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def traversal(inorder, postorder):
            # 数组大小为0，则代表空节点
            if len(postorder) == 0:
                return None

            # 后序遍历数组的最后一个元素为根节点的值
            root_val = postorder[-1]
            root = TreeNode(root_val)

            # 以根节点切割中序遍历数组
            delimiter_index = inorder.index(root_val)
            
            # 切割中序遍历数组，得到左右子树
            left_inorder = inorder[:delimiter_index]
            right_inorder = inorder[delimiter_index + 1:]

            # 按照上一步骤的结果切割后序遍历数组，对于每一部分都取最后一个元素，
            # 则为该子树的根节点的值
            left_length = len(left_inorder)
            right_length = len(right_inorder)
            left_postorder = postorder[:left_length]
            right_postorder = postorder[left_length: left_length + right_length]

            # 递归两个部分
            root.left = traversal(left_inorder, left_postorder)
            root.right = traversal(right_inorder, right_postorder)

            return root
        
        if len(inorder) ==0 or len(postorder) == 0:
            return None
        return traversal(inorder, postorder)
    
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def traversal(inorder, postorder):
            if len(postorder) == 0:
                return None
            # 根的值就是 postorder 中最后一个元素的值
            root_val = postorder[-1]
            root = TreeNode(root_val)
            # 在 inorder/postorder 中根据 root_val 确定左右子树的 sublist
            root_idx = inorder.index(root_val)
            left_inorder = inorder[:root_idx]
            right_inorder = inorder[root_idx + 1:]
            # 根据 inorder 的长度来切割 postorder
            left_postorder = postorder[:len(left_inorder)]
            right_postorder = postorder[len(left_inorder):-1]
            # 构造左右子树
            root.left = traversal(left_inorder, left_postorder)
            root.right = traversal(right_inorder, right_postorder)
            # 返回结果
            return root
        
        return traversal(inorder, postorder)