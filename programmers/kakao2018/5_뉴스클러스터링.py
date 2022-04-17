"""
1. Handle string
"""
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    str1 = [str1[i:i+2] for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2] for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
   
    intersection = set(str1) & set(str2)
    union = set(str1) | set(str2)
   
    intersection = [min(str1.count(i), str2.count(i)) for i in intersection]
    union = [max(str1.count(i), str2.count(i)) for i in union]
   
    return int(sum(intersection) / sum(union) * 65536) if len(str1 + str2) != 0 else 65536
