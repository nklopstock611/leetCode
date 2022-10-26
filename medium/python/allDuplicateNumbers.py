def findDuplicates(nums):
    duplicates = {}
    for val in nums:
        if val in duplicates:
            duplicates[val] += 1
        else:
            duplicates[val] = 1
    
    answer = []
    for val in duplicates:
        if duplicates[val] >= 2:
            answer.append(val)

    answer.sort()
    return answer

l = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(l))