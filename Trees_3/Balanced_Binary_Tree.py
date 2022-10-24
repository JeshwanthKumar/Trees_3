# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Complexity: O(n)
#Space_Complexity: Recursive stack space - O(n)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True    #Initialize falg as true
        self.balance(root)  #Recursion
        return self.flag    #Return flag
        
    def balance(self, root):
        #base condtion
        if root == None:     #If the root is none the return 0 which unfolds the recursion 
            return 0
        
        leftHeight = self.balance(root.left)    #Calculate the left height of the tree by recursively calling balance(root.left)
        rightHeight = self.balance(root.right)  #Calculate the right height of the tree by recursively calling balance(root.right)
        
        if abs(leftHeight - rightHeight) > 1:   #If the absolute difference between the left height and right height is greater than 1 then change the flag to false
            self.flag = False
            
        return 1+max(leftHeight, rightHeight)   #Return 1+ maximum between the left and right height
        