from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day, days, last = [0] * 366, set(days), days[-1]
        for i in range(1, last + 1):
            if i not in days:
                day[i] = day[i - 1]
            else:
                day[i] = min(day[i - 1] + costs[0], day[i - 7 if i >= 7 else 0] + costs[1],
                             day[i - 30 if i >= 30 else 0] + costs[2])
        return day[last]

    def mincost_tickets(self, days: List[int], costs: List[int]) -> int:
        # Initialize an array to store the minimum cost for each day
        dp = [0] * 366
        # Mark the travel day with 1
        travel_days = set(days)
        # Solve the sub problem from day 1 to day 365
        for i in range(1, 366):
            if i not in travel_days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
        return dp[days[-1]]

if __name__ == '__main__':
    zhushi = Solution()
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    print(zhushi.mincost_tickets(days, costs))