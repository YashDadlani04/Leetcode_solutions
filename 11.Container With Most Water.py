class Solution:
    def maxArea(self, height: List[int]) -> int:
        L=0
        R= len(height) -1
        max_area=0

        while(L<R):
            h= min(height[L], height[R])
            w= R-L
            area=h*w
            max_area= max(area, max_area)

            if(height[L]>=height[R]):
                R-=1
            else:
                L+=1
        return max_area

        