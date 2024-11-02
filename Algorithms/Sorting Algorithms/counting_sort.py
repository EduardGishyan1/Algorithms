from typing import List

def counting_sort(nums:List[int]):
    max_val = max(nums) + 1
    counts = [0] * max_val
    
    for i in nums:
        counts[i] += 1
    
    output = []
    for i in range(len(counts)):
        output.extend([i]*counts[i])
    
    return output