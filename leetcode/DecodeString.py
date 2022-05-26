class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '' or s.isalpha(): return s

        idx = 0
        if s[0].isdigit():
            while s[idx].isdigit():
                idx += 1
            return int(s[:idx]) * self.decodeString(s[idx + 1:self.find_balanced_brackets(s)]) + \ 
                self.decodeString(s[self.find_balanced_brackets(s) + 1:])
        else: # s[0].isalpha() == True
            while s[idx].isalpha():
                idx += 1
            return s[:idx] + self.decodeString(s[idx:])


    def find_balanced_brackets(self, s):
        state = 0
        for idx in range(1,len(s)):
            if s[idx] == '[': state += 1
            elif s[idx] == ']': state -= 1
            else: continue
            if state == 0: return idx
            
        
            
