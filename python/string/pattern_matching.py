

class Solution:
    
    
    def findAndReplacePattern(self, words, pattern):
        '''
        :type words: list of str
        :type pattern: str
        :rtype: list of str
        '''
        matches = []
        # len is length of the
        # pattern
        Len = len(pattern)
 
        # Encode the string
        hash = self.encodeString(pattern)
 
        #Iterate through the array of strings
        for word in words:
 
            #If the returned hash is same and size is same than append to ans
            if(len(word) == Len and
                self.encodeString(word) == hash):
                matches.append(word)
        return matches
        
    def encodeString(self,Str):
   
        map = {}
        res = ""
        i = 0
 
        #Iterate through each character in the given string
        for ch in Str:

            #If the char is occuring first time , assign next unique number to it
            if ch not in map:
                map[ch] = i
                i += 1
             
            
            res += str(map[ch])
        return res

sol = Solution()
words = ["zcc", "bbc", "bcb", "yzy"]
pattern = "hhv"
print(sol.findAndReplacePattern(words, pattern))

        