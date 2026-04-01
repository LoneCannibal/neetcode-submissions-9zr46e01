class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r,res=1,max(piles),1
        while(l<=r):
            m = (l+r)//2
            total_duration = 0
            for i in piles:
                total_duration = total_duration + math.ceil(i/m) 
            if (total_duration > h):
                l=m+1
            else:
                res = m
                r = m-1
        return res 
        