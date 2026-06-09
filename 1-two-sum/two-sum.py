class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        for p in range(len(nums)):
            current_map_val=nums_map.get(nums[p])
            if current_map_val is not None:
                return [current_map_val,p]
            else:
                number_to_find=target-nums[p]
                nums_map[number_to_find]=p
        
        return None
        
        