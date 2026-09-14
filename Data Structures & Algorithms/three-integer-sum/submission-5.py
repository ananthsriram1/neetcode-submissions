"""
[-4, -1, -1, 0, 1, 2]

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        rv = []
        uid = set()
        num_map = defaultdict(list)
        for i in range(len(nums)):
            num_map[nums[i]].append(i)
        print(num_map)

        for i in range(0, len(nums) - 2):
            first = nums[i]
            for j in range(i + 1, len(nums) - 1):
                  
                second = nums[j]
                
                remainder = 0 - first - second

                if remainder in num_map and num_map[remainder][-1] > j:
                    
                    tup = (first, second, remainder)
 
                    if tup in uid:
                        continue
                    uid.add(tup)
                    rv.append(tup)

        return rv