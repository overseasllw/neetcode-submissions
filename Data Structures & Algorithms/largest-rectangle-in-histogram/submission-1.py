class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = None
        for i, height in enumerate(heights):
            tmp = None

            while stack and height <= stack[-1][1]:
                tmp = stack.pop()
            stack.append((tmp[0] if tmp is not None else i,height))
            area = max((i - j +1) * min(h, height) for j, h in stack)

            if maxArea is None or maxArea < area:
                maxArea = area

        return maxArea