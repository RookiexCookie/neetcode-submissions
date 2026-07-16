class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod=1
        answer = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                prod*=nums[j]
            answer.append(prod)
            prod=1
        return answer  