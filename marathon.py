from operator import eq


def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    flag = True

    for i in range(len(completion)):
        if not eq(participant[i], completion[i]):
            answer = participant[i]
            flag = False
            break
    if flag:
        answer = participant[len(participant) - 1]

    return answer
