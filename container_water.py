class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_val = 0
        
        while left < right:
            current_height = min(height[left], height[right])
            width = right - left
            current_area = current_height * width
            
            if current_area > max_val:
                max_val = current_area
                
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_val