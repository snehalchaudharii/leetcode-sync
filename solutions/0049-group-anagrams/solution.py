class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time complexity as O(m * n log n) space complexity O(m * n)
        # anagrams = defaultdict(list)
        # for s in strs:
        #     key = "".join(sorted(s))
        #     anagrams[key].append(s)
        # return list(anagrams.values())

        # TC: O(n * k) SC: O(nk)

        anagrams = defaultdict(list)

        for word in strs:
            freq = [0] * 26  # Frequency array for 'a' to 'z'
            for char in word:
                freq[ord(char) - ord('a')] += 1  # Count occurrences
            
            freq_key = tuple(freq)  # Convert list to string
            anagrams[freq_key].append(word)  # Use string representation as key
        
        return list(anagrams.values())
