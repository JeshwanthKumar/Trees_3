# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Complexity: O(n)
#Space_Complexity: Recursive stack space - O(n)


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = -1001    #Initialize maximum greater than maximum limit given
        self.path(root)     #Recursion call
        
        return self.maximum     #Return maximum to get the maximum path sum
    
    
    def path(self, root):
        #base condition
        if root == None: #If the root is none the return 0 which unfolds the recursion
            return 0
        
        leftSum = max(0, self.path(root.left))  #Calculate leftSUm by choosing between 0 and recursive call of root.left which is maximum so that the maximum path sum is achieved
        rightSum = max(0, self.path(root.right))    #Calculate rightSum by choosing between 0 and recursive call of root.right which is maximum so that the maximum path sum is achieved
        
        rootMax = root.val + leftSum + rightSum #Calculate rootMax by adding root.val with both leftSum and rightSum
        
        if self.maximum < rootMax:  #If the maxmimum is less than rootMax then change the maximum value to rootMax
            self.maximum = rootMax
            
        return root.val + max(leftSum, rightSum)    #Return the sum of max between leftSum and rightSum