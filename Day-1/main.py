def mergeAlternately(word1, word2):
    merged = []
    l1 = len(word1)
    l2 = len(word2)
    i, j = 0, 0
    while i < l1 and j < l2:
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    merged.extend(word1[i:])
    merged.extend(word2[j:])
    result = "".join(merged)
    return result
