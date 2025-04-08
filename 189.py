def solution(nums,k):
    remainder = k % len(nums) 
    array1 = nums[0:len(nums)-remainder]
    array2 = nums[(len(nums)-remainder):len(nums)]

    # Update 0 index to k elements
    for index, item in enumerate(array2):
        nums[index] = item
    # Update the last remaining elements
    for index, item in enumerate(array1):
        nums[index+remainder] = item