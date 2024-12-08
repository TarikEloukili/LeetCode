class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter=0
        if nums ==[] or nums ==[0]:
            return 0
        
        elif len(nums)==1:
            return 1
        
        while sum(nums)!=0:
            minimum = float('inf')
            for i in range(len(nums)):
                if nums[i]<minimum and nums[i]!=0:
                    minimum=nums[i]

            for j in range(len(nums)):
                if nums[j]!=0:
                    nums[j]-=minimum
            counter+=1
        return counter
            
            
                
            
            