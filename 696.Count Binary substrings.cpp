// 19*02*2026(was marked easy but WAS NOT EASY)

class Solution {
public:
    int countBinarySubstrings(string s) {
        int n= s.length();
        
        int ans =0;
        int prev=0;
        int curr= 1;

        for(int i = 1; i<n; i++) {
            if(s[i-1] == s[i]) {
                curr++;           
            } 
            else {
                ans += min(prev, curr);
                prev = curr;
                curr = 1;
            }
        }        
        return ans + min(prev, curr);        
    }
};