def solution(progresses, speeds):
    answer = []
    while len(progresses):
        flag = False
        complete = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while len(progresses) != 0 and progresses[0] >= 100:
            flag = True
            complete += 1
            del progresses[0]
            del speeds[0]
        if flag is True:
            answer.append(complete)
    return answer
