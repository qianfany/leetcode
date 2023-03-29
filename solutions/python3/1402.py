from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # First, sort the satisfaction values in ascending order
        satisfaction.sort()

        # Initialize variables
        max_satisfaction = 0
        total_satisfaction = 0
        current_satisfaction = 0

        # Iterate through the sorted satisfaction values, starting from the last element
        for s in reversed(satisfaction):
            # Calculate the new total satisfaction by adding the current value
            total_satisfaction += s

            # If the new total satisfaction is positive,
            # update the current satisfaction and max satisfaction
            if total_satisfaction > 0:
                current_satisfaction += total_satisfaction
                max_satisfaction = max(max_satisfaction, current_satisfaction)
            else:
                # If the new total satisfaction is negative, stop the iteration
                break

        return max_satisfaction

if __name__ == '__main__':
    zhushi = Solution()
    list = [-1, -8, 0, 5, -9]
    print(zhushi.maxSatisfaction(list))
