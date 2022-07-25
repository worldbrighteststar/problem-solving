"""
1. Hash Map
"""
def solution(record):
    answer = []
    actions = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    user_map = dict()
    
    for each in record:
        infos = each.split()
        
        if infos[0] != 'Leave':
            user_map[infos[1]] = infos[2]
        if infos[0] != 'Change':
            answer.append([infos[1], actions[infos[0]]])
    
    return [''.join([user_map[each[0]], each[1]]) for each in answer]
