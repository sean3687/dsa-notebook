# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# order :does't matter : 0,1,3,0,4,
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# class Solution:
def removeElement(nums, val):
    # Objective
    # 1. remove the vals in nums array
    # 2. we are returning the length of nums after removal

    # receving nums and val
    # we have to go through nums and check each element if == val
    # for index,item in enumerate(nums):
      # item == val

    # key = 0 : value : item value 

    # 0 : 0
    # 1 : 1
    # 2 : 3
    # 3 : 0
    # 4 : 4


    # nums = [0,1,2,2,3,0,4,2],
  #.          0,1,3,0,4
    # for index, item in enumerate(nums):
    #   # for key, value in d.items():
    #     if index in d:
    #       nums[index] = d[index] 
    #     else: 
    #       nums.pop()

    # return len(d)

  d = {}
  curr = 0
  # Record new nums array in hashmap
  for index, item in enumerate(nums):
    if item == val:
      continue
    else:
      d[curr] = item
      curr = curr+1
  print(d)
      
    

  for index in range(0, len(nums)):
    print("--")
    print("index:",index)
    if index in d:
        nums[index] = d[index]
        print("1")
    else:
      nums.pop()
      print("2")
    print(nums)
  return len(d)
  
nums = [0,1,2,2,3,0,4,2]
print(removeElement(nums,2))
print(nums)

# official soln
def removeElement(self, nums: List[int], val: int) -> int:
  # i is non val
  i = 0
  for j in range(len(nums)):
      if nums[j] != val:
          nums[i] = nums[j]
          i += 1
  return i


class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
      left, right = 0, 0

      while right < len(nums):
          if nums[right] != val:
              nums[left] = nums[right]
              left += 1

          right += 1

      return left

    
        
      
      
      
    
    
    
    

