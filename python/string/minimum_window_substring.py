import sys

class Solution:
    def minWindow(self, searchString, t):
        '''
        :type searchString: str
        :type t: str
        :rtype: str
        '''
        n = len(searchString)
        
        # It contains the min length seen so far
        min_window_size = len(searchString)
        # min_window_size = sys.maxsize
        
        # It contains the minimum length substring
        min_window = ""
        
        # The nested for loop help us generate all the substrings
        for left in range(0, n):
            for right in range(left, n):

                # Generate the substring
                window_snippet = searchString[left : right + 1]
                
                # Check if the generated char contains all the characters of target
                window_contains_all = self.contains_all(window_snippet, t)
                
                # If it is a valid substring
                # And the length is less than the minimum so far
                # Update the answer
                if window_contains_all and len(window_snippet) < min_window_size:
                    min_window_size = len(window_snippet)
                    min_window = window_snippet
        
        return min_window
        
    # Helper function to check if all the char of string are
    # Present in the string searchString
    def contains_all(self, searchString, t):
        required_characters = {}
        
        for i in range(0, len(t)):
            occurrences = 0
            if t[i] in required_characters:
                occurrences = required_characters[t[i]]
                
            required_characters[t[i]] = occurrences + 1
        
        for i in range(0, len(searchString)):
            curr = searchString[i]
            
            if curr in required_characters:
                # Calculate what the new occurrence count will be
                new_occurrences = required_characters[curr] - 1
                
                """
                If we have satisfied all of the characters for this character, remove the key
                from the hashtable.
                 
                Otherwise, just update the mapping with 1 less occurrence to satisfy for
                """ 
                
                if new_occurrences == 0:
                    del required_characters[curr]
                else:
                    required_characters[curr] = new_occurrences
                    
        
        """
        If we satisfied all characters the the required characters hashtable will be
        empty
        """
        return not required_characters

s = Solution()
print(s.minWindow('aaat', 't'))
print(s.minWindow('adobecodebanc', 'abc'))
print(s.minWindow('hello', 'hel'))