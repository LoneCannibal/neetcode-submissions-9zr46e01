class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1,l2,final=m-1,n-1,m+n-1
        while(l1>=0 and l2>=0):
            if(nums1[l1] > nums2[l2]):
                nums1[final] = nums1[l1]
                final-=1
                l1-=1
            else:
                nums1[final]=nums2[l2]
                final-=1
                l2-=1
            print(nums1)
        if(l1>0):
            while(l1>=0):
                nums1[final] = nums1[l1]
                final-=1
                l1-=1
        else:
            while(l2>=0):
                nums1[final]=nums2[l2]
                final-=1
                l2-=1

        