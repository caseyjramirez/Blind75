# returns true if any values in the array are duplicate
# returns false if all values are unique.
class Solution(object):
    test1 = [1, 1]

    def containsDuplicate(nums):
        hashset = set();
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n);
    
    
    containsDuplicate(test1);