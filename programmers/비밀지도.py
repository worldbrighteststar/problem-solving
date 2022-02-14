"""
1. Decimal to Binary
"""
def solution(n, arr1, arr2):
    answer = []


    def dec_to_bin(num):
        """
        input : decimal number (int)
        output : binary number (list)
        """
        return dec_to_bin(num//2) + str(num%2) if num > 0 else ''


    for n1, n2 in zip(arr1, arr2):
        n1_map, n2_map = dec_to_bin(n1).zfill(n), dec_to_bin(n2).zfill(n)
        merged_map = [' ' if n1_map[i] + n2_map[i] == "00" else '#' for i in range(n)]
        answer.append(''.join(merged_map))
    
    return answer
