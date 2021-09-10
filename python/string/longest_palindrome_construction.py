def longestPalindrome(self, s):
    '''
    :type s: str
    :rtype: int
    '''
    matches = {} # to track characters matching
    counter = 0 # to count matching characters
    for  index, char in enumerate(s):
        #index is optional simply to store key values in dict
        # if char from string not in matches we gonna store for first time
        if char not in matches:
            matches[char] = index
        # if char already in matches that means we got the matching so we update a counter as 
        # two pair and delete the character from the matches for new entry
        else:
            counter += 2
            del matches[char]
    # if remaing character which doesn't get matching and counter > 1
    if matches:
        counter += 1
    return counter

