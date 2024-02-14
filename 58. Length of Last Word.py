class Solution:
    def lengthOfLastWord(self, s):
        last=s.split()
        m=len(last)
        n=len(last[m-1])
        return n
        