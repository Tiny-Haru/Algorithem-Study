def solution(priorities, location):
    answer = len(priorities)
    array = []
    for i in range(len(priorities)):
        array.append(i)

    while location in array:
        paper = priorities.pop(0)
        idx_paper = array.pop(0)
        maxCheck = False
        for i in range(len(priorities)):
            if paper < priorities[i]:
                maxCheck = True
                break
        if maxCheck:
            priorities.append(paper)
            array.append(idx_paper)

    return answer - len(array)


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
