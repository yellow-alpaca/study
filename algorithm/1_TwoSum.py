class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        targetが加算して成立する一意の組み合わせを返す。
        dictのkeyにnumsが持つ値を、valueに位置を保管し、
        式の成立する値をハッシュを使って検索する。
        from LEETCODE (1.Two Sum)
        https://leetcode.com/problems/two-sum/
        """
        # Time: O(n)
        # Space: O(n)
        hashmap = {}
        for current_index in range(len(nums)):
            complement = target - nums[current_index]
            if complement in hashmap:
                return [hashmap[complement], current_index]
            else:
                hashmap[nums[current_index]] = current_index
