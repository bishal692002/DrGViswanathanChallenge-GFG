# User function Template for Python3

class Solution:
    def floorSqrt(self, n): 
        if n == 0 or n == 1:
            return n  # Base case

        left, right = 1, n
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == n:
                return mid  # Perfect square case
            elif mid * mid < n:
                ans = mid  # Store possible answer
                left = mid + 1  # Move to right half
            else:
                right = mid - 1  # Move to left half

        return ans  # Floor value of sqrt(n)




