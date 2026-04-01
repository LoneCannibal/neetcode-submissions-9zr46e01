class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        current,next=0,1
        while(next<len(nums)):
            if(nums[current] == nums[next]):
                nums.pop(next)
            else:
                current = next
                next += 1
        return len(nums)
