class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # n = int("".join(map(str, num)))
        
        # total = n + k

        # return list(map(int, str(total)))

        i = len(num) - 1
        carry = k
        result = []

        # Process from rightmost digit, carry handles k as well
        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
                i -= 1
            result.append(carry % 10)
            carry //= 10

        return result[::-1]
