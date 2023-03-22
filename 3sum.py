class Solution:

  def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    n = len(nums)

    for i in range(n - 2):
      # skip duplicates
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      # two-pointer approach to find pairs
      left, right = i + 1, n - 1

      while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
          result.append([nums[i], nums[left], nums[right]])

          # skip duplicates
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          while left < right and nums[right] == nums[right - 1]:
            right -= 1

          left += 1
          right -= 1
        elif total < 0:
          left += 1
        else:
          right -= 1

    return result
