class Solution { 
public:  
     int solve(TreeNode* root, int val) {
        if(root == NULL) { 
            return 0;
        }

        val = (2*val) +  pow(2,0) * (root->val);

        if(root->left == NULL && root->right == NULL)
            return val;
        
        return solve(root->left, val) + solve(root->right, val);
    }
    int sumRootToLeaf(TreeNode* root) {
        return solve(root, 0);
        
    }
};
// Using leap of faith RECURSSION

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, val):
            if not node:
                return 0
            
            val = (val << 1) | node.val
            
            if not node.left and not node.right:
                return val
            
            return dfs(node.left, val) + dfs(node.right, val)
        
        return dfs(root, 0)