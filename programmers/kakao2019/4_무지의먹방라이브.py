"""
1. Binary Search
"""

def solution(food_times, k):
    if sum(food_times) <= k: 
        return -1
    
    mn_food, mx_food = 0, max(food_times)
    while mn_food < mx_food - 1: # binary search
        mid = (mn_food + mx_food) // 2
        if get_time_for_eating(food_times, mid) <= k:
            mn_food = mid
        else:
            mx_food = mid
            
    # return remain_food_list[remain second]
    return [i + 1 for i, f in enumerate(food_times) if f - mn_food > 0][k - get_time_for_eating(food_times, mn_food)]

def get_time_for_eating(food_times, x):
    """
    input : food_times(list), x(seconds)
    output : time of eating each food x times
    """
    return sum([x if f >= x else f for f in food_times])
