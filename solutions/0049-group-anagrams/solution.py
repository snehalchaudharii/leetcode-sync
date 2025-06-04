class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        # TC: O(n * k) SC: O(nk)
        # N = Number of words
# k = Length of the longest word (for building frequency array)

# The defaultdict(list) ensures that if a key does not exist, it is automatically assigned an empty list ([]).
        anagrams = defaultdict(list)

        for word in strs:
            freq = [0] * 26  # Frequency array for 'a' to 'z'
            for char in word:
                freq[ord(char) - ord('a')] += 1  # Count occurrences
            # Tuple keys are immutable and correctly represent frequency distributions without unintended transformations
            freq_key = tuple(freq)  # Convert list to tuple which hashable and maintains order correctly):
            anagrams[freq_key].append(word)  # Use string representation as key
        
        return list(anagrams.values())
