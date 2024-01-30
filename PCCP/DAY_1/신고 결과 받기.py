def solution(id_list, report, k):
    answer = []
    
    memo = [[0] * len(id_list) for i in id_list]
    
    for rep in report:
        a, b = rep.split(' ')
        a_idx = id_list.index(a) # reporter
        b_idx = id_list.index(b) # reported
    
        memo[a_idx][b_idx] = 1
    
    list = [] # 정지 받는 유저 idx
    for user_idx in range(len(id_list)):
        count = 0
        for i in range(len(id_list)):
            count += memo[i][user_idx]
        if count >= k:
            list.append(user_idx)
    
    # 신고 메일 수
    for user_idx in range(len(id_list)):
        count = 0
        for li in list:
            count += memo[user_idx][li]
        answer.append(count)
    
    # 한 번에 한 명의 유저를 신고
    # 신고 횟수에 제한은 없습니다
    # 한 유저를 여러 번 신고할 수도 있지만 1회로 처리
    
    # k번 이상 신고된 유저 : 정지 + 정지 메일(신고 내용을 취합) 발송

    return answer