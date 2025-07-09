class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_t= Counter(t)
        count_s= Counter(s)

        for ch in count_t:
            if count_t[ch]> count_s.get(ch, 0):
                return ch
