class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = list(range(1, max(nums)))
        temp3 = []

        for element in nums2:
            if element not in nums:
                temp3.append(element)
        print(temp3)

nums = [4,3,2,7,8,2,3,1]
numss = [1,1]
s = Solution()
s.findDisappearedNumbers(numss)

