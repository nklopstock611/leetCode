def arrayStringsAreEqual(word1, word2):
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """
    s1 = ""
    for val in word1:
        s1 += val
        
    s2 = ""
    for val in word2:
        s2 += val
        
    answer = False
    if s1 == s2:
        answer = True
    
    return answer