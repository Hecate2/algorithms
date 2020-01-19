'''
List Mode:
Runtime: 40 ms, faster than 97.87% of Python3 online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 53.95% of Python3 online submissions for Two Sum.
'''

'''
Tuple Mode:
Runtime: 52 ms, faster than 53.96% of Python3 online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 51.63% of Python3 online submissions for Two Sum.
'''

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

[3,3]
6
->[0,1]

[3,2,4]
6
->[1,2]
'''

#Dictionary, or 'hashmap' implemented

#Some fast solutions involved sorting the input list. Interesting.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums=tuple(nums)
        length=len(nums)
        map={}  #{值:下标}组成的字典 #nums[i]:i for i in range(length)
        for i in range(length): #遍历数组nums
            num=nums[i]
            counterpart=target-num
            if counterpart in map:
                return [map[target-num],i]
            map[num]=i
