class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res=0
        l,r=0,len(height)-1
        leftmax,righttmax=height[l],height[r]
        while l<r:
            if leftmax < righttmax:
                l+=1
                leftmax=max(leftmax,height[l])
                res += leftmax-height[l]
            else:
                r-=1
                righttmax=max(righttmax,height[r])
                res+= righttmax-height[r]
        return res