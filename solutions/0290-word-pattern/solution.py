class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words= s.split(" ")
        freqlettertoword={}
        freqwordtoletter={}

        if len(pattern) != len(words):
            return False

        for letter, word in zip(pattern, words):
            if letter not in freqlettertoword and word not in freqwordtoletter:
                freqlettertoword[letter]= word
                freqwordtoletter[word]= letter
            elif freqlettertoword.get(letter)!= word or freqwordtoletter.get(word)!=letter:
                return False
        return True
