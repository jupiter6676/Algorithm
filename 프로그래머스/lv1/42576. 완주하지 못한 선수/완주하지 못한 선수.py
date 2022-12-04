def solution(participant, completion):
    answer = ''
    
    p_dict = {}
    
    for elem in participant:
        p_dict[elem] = p_dict.get(elem, 0) + 1
        
    for elem in completion:
        p_dict[elem] -= 1
    
    for k, v in p_dict.items():
        if v > 0:
            answer = k
            break
    
    return answer