'''
Runtime: 56 ms, faster than 75.06% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''

'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):  #s for the input string
        #detect new substrings with a sliding window
        
        map = {}  #stores all the characters found in the substring
        #{character:position_in_the_input_string}

        maxlen = 0  #the answer
        start = 0 #the starting point of the sliding window
        for i,value in enumerate(s):    #'abc' -> 0 a; 1 b; 2 c
            if value in map:
                #Repeating character found.
                #Change the starting position of the sliding window
                #to the next character of the repeated one.
                new_start = map[value] + 1
                if new_start > start:
                    start = new_start
            #no repeating character found,
            #or have renewed the start of the sliding window
            num = i - start + 1
            maxlen=max(maxlen,num)
            map[value] = i
            
        return maxlen
