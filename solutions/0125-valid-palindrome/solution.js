var isPalindrome = function(s) {
    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        // skip non-alphanumeric on left
        while (left < right && !isAlphaNum(s[left])) {
            left++;
        }

        // skip non-alphanumeric on right
        while (left < right && !isAlphaNum(s[right])) {
            right--;
        }

        // compare lowercase characters
        if (s[left].toLowerCase() !== s[right].toLowerCase()) {
            return false;
        }

        left++;
        right--;
    }

    return true;
};

// helper function: checks if char is alphanumeric
function isAlphaNum(c) {
    return /[a-z0-9]/i.test(c);
}

    
    // O(n) & O(n)
    // let clean = s.toLowerCase().replace(/[^a-z0-9]/g, "");
    // let reversed = clean.split("").reverse().join("");
    // return clean === reversed;
    

