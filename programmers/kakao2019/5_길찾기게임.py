"""
1. DFS
"""
from collections import defaultdict, deque
import sys;sys.setrecursionlimit(10000)

def solution(nodeinfo):
    nodeinfo = [node + [i+1] for i, node in enumerate(nodeinfo)] # numbering
    nodeinfo = deque(sorted(nodeinfo, key=lambda x: (-x[1], x[0]))) # order by y, x
    T = defaultdict(list)
    wait_list = [(0, 100000, '*')] # parents list waiting for a child 
    head = nodeinfo[0][2]
    
    while nodeinfo:
        x, y, n = nodeinfo.popleft()
        
        for parents_info in wait_list: # search parents node by x-range
            x_mn, x_mx, parents_node = parents_info
            
            if x_mn <= x <= x_mx:
                T[parents_node].append(n)
                wait_list += [(x_mn, x-1, n),(x+1, x_mx, n)]
                wait_list.remove(parents_info)
                break
    
    return travers(T, [], [], head)


def travers(input_dict, pre_order, post_order, node):
    """
    input : binary tree (dict)
    output : [[pre-order], [post-order]] (list)
    """
    pre_order.append(node)
    
    for next_node in input_dict[node]:
        travers(input_dict, pre_order, post_order, next_node)
        
    post_order.append(node)    
    
    return [pre_order, post_order]
