# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        res = []

        for item in nums: 
            if item in d:
                if d[item] >= 2:
                    # Over limit, skip
                    d[item] += 1
                    print("step1:", item)
                else:
                    res.append(item)
                    d[item] += 1
                    print("step2:", item)
            else:
                d[item] = 1
                res.append(item)
                print("step3:", item)


        for i in range(len(res)):
            nums[i] = res[i]
        print(res)
        return len(res)
