def solution(height):
  l,r = 0, len(height)-1
  max_area = 0

  while l < r:
    width = r-l
    h = min(height[r], height[l])
    area = width * h
    max_area = max(max_area, area)

    # Move each pointer
    if height[l] < height[r]:
      l = l +1

    # move right pointer to left
    else:
      r = r-1
  return max_area

heights = [1,8,6,2,5,4,8,9,7]
solution(heights)