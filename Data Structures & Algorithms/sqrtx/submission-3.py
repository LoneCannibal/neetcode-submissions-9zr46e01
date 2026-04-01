class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        res=0
        r=x
        while(l<=r):
            mid =int((l+r)/2)
            print(mid)
            if(mid*mid<x):
                l=mid+1
                res =mid
            elif(mid*mid >x):
                r=mid-1
            else:
                return mid
        return res



        