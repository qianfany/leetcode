class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        distinct = set()
        slow = 0
        fast = 0
        longest = 0

        while fast < len(s):
            if s[fast] in distinct:
                distinct.remove(s[slow])
                slow += 1
            else:
                distinct.add(s[fast])
                fast += 1
                longest = max(longest, fast - slow)
        return longest


