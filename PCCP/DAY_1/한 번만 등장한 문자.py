def solution(s):
    answer = ''
    arr = [0] * 26
    
    for ch in s:
        arr[ord(ch) - ord('a')] += 1
    
    # 한 번만 등장하는 문자
    for idx, val in enumerate(arr):
        if val == 1:
            answer += chr(idx + ord('a'))
    return answer