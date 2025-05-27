def solution(height):
  l,r = 0, len(height)-1
  max_area = 0
  
  while l < r:
      max_area = max(max_area, min(height[l], height[r]) * (r - l))
      if height[l] < height[r]:
          l += 1
          else:
              r -= 1

              return max_area

# Solution2:

if not height:
    return 0

    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)

        if height[left] < height[right]:
            left += 1
            else:
                right -= 1

                return max_area