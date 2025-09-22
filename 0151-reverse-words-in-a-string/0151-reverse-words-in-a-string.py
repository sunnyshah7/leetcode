class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        i = len(s) - 1
        
        while i >= 0:
            # Skip trailing spaces
            while i >= 0 and s[i] == ' ':
                i -= 1
            
            if i < 0:
                break
            
            # Find end of word
            end = i
            
            # Find start of word
            while i >= 0 and s[i] != ' ':
                i -= 1
            start = i + 1
            
            # Append this word to res
            res.append(s[start:end+1])
            
        # Join with single spaces
        return " ".join(res)
        