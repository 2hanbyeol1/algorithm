def solution(survey, choices):
    answer = ''
    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    choice_score = [-1, 3, 2, 1, 0, 1, 2, 3]
    for i in range(len(survey)):
        char_disagree = survey[i][0]
        char_agree = survey[i][1]
        choice = choices[i]
        if choice < 4: # 비동의
            score[char_disagree] += choice_score[choice]
        elif choice > 4: # 동의
            score[char_agree] += choice_score[choice]
    for pair1, pair2 in pairs:
        if score[pair1] >= score[pair2]:
            answer += pair1
        else:
            answer += pair2
    return answer