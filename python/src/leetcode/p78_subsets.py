class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        for each element of list, there is two option add it the set or not.
        """



        def subsets(nums, sets):
            if not nums:
                return sets
            next = nums[0]

            # this element is not added
            sets1 = subsets(nums[1:], sets)

            # this element is added added
            inserted_sets = [ s.append(next) for s in sets]

            sets2 = subsets(nums[1:], inserted_sets)

            return sets1 + sets2

        return subsets(nums, [[]])
