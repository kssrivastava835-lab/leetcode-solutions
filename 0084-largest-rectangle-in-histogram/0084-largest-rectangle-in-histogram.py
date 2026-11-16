class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)
        for i in range(n + 1):
            current_height = heights[i] if i < n else 0
            while stack and current_height < heights[stack[-1]]:
                height = heights[stack.pop()]
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary -1 
                area = height * width
                max_area = max(max_area , area)
            
            if i < n :
                stack.append(i)

        return max_area

