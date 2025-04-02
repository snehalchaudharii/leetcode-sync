class RandomizedSet:
    def __init__(self):
        self.vals = []  # List to store values
        self.val_to_index = {}  # Map value to its index in vals

    def insert(self, val: int) -> bool:
        # If value already exists, return False
        if val in self.val_to_index:
            return False
        # Add to list and record index
        self.val_to_index[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        # If value not present, return False
        if val not in self.val_to_index:
            return False
        # Get index of value to remove
        index = self.val_to_index[val]
        last_val = self.vals[-1]
        # Swap with last element if not already last
        if index != len(self.vals) - 1:
            self.vals[index] = last_val
            self.val_to_index[last_val] = index
        # Remove last element
        self.vals.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        # Return random element from list
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
