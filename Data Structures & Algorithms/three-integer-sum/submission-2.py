class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        previ=None
        
        for i in range(len(nums)-1):
            if previ is not None and nums[i] == previ:
                continue
            l,r = i+1,len(nums)-1
            while(l<r):
                if(nums[l] + nums[r] + nums[i] == 0):
                    temp=[nums[i],nums[l],nums[r]]
                    res.append(temp)
                    t=l+1
                    while(nums[t] == nums[l] and t<len(nums)-1):
                        t+=1
                    l=t

                elif nums[l]+nums[r]+nums[i] > 0:
                    t=r-1
                    while(nums[t] == nums[r] and t>=0):
                        t-=1
                    r=t
                else:
                    t=l+1
                    while(nums[t] == nums[l] and t<len(nums)-1):
                        t+=1
                    l=t
            previ=nums[i]
        return res

