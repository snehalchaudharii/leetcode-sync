class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Step 1: Create a frequency dictionary for 't'
        target_counts = {}  
        for char in t:
            target_counts[char] = target_counts.get(char, 0) + 1  
        required_chars = len(target_counts)  # Unique characters in t that must be in the window

        # Step 2: Initialize window pointers and helper variables
        left, right = 0, 0  # Pointers for the sliding window
        formed = 0  # Count of unique chars in window that match t's frequency
        window_counts = {}  # Frequency of characters in current window
        min_length = float("inf")  # Initialize minimum length to infinity
        min_window = ""  # Store the final result

        # Step 3: Expand the window by moving 'right'
        while right < len(s):
            char = s[right]  # Character at 'right' index
            window_counts[char] = window_counts.get(char, 0) + 1  # Add to window frequency

            # If char's frequency matches the target count, increase 'formed'
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1  

            # Step 4: Contract the window from the left
            while left <= right and formed == required_chars:
                char = s[left]  # Character at 'left' index

                # Update minimum window substring if a smaller valid window is found
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right + 1]

                # Shrink the window from the left
                window_counts[char] -= 1  
                if char in target_counts and window_counts[char] < target_counts[char]:
                    formed -= 1  # If a required char is removed, reduce 'formed'

                left += 1  # Move left pointer forward

            right += 1  # Move right pointer forward
        
        return min_window
