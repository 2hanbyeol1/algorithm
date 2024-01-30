def solution(s):
    answer = s
    
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx, value in enumerate(num):
        answer = answer.replace(value, str(idx))
        
    return int(answer)