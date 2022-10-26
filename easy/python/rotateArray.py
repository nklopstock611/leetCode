def rotate(nums: list, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    reversed = nums[::-1]
    while i < k:
        last_val = reversed[0]
        reversed.append(last_val)
        ind = reversed.index(last_val)
        reversed.pop(0)
        
        i += 1
        
    diff = len(reversed) - len(nums)
    if diff > 0:
        reversed = reversed[:len(reversed) - diff]
    
    nums.clear()
    
    for val in reversed[::-1]:
        nums.append(val)