class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        store=s.strip().split(" ")
        return len(store[-1])
