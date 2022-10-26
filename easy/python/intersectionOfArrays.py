def intersection(nums1: list, nums2: list) -> list:
    s1 = set()
    s2 = set()
    
    for val in nums1:
        s1.add(val)
        
    for val in nums2:
        s2.add(val)
        
    answer = list(s1.intersection(s2))
    
    return answer