from typing import List

def insertion_sort(nums: List[int]) -> None:
    for i in range(len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j] , nums[j+1] = nums[j+1],nums[j]
            j -= 1
        nums[j+1] = key