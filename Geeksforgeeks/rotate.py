class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1


    def rotate(self, nums, k) -> None:
        n = len(nums)
        k %= n
        print(k)

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        return nums

list_a=[1,2,3,4,5,6,7]
b = Solution()
print(b.rotate(list_a,2))
