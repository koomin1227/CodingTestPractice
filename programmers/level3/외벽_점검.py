from itertools import permutations
def solution(n, weak, dist):
    answer = 0
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    for start in range(length * 2):
        for perm in list(permutations(dist, len(dist))):

            person = len(dist) - 1
            cover = weak[start] + perm[person]
            count = 0
            for cur in range(start, length * 2):
                if weak[cur] > cover:
                    person -= 1
                    cover = weak[cur] + perm[person]
                    if person < 0:
                        break
                count += 1
                if count == length:
                    answer = min(answer, len(dist) - person)
                    break

    if answer == len(dist) + 1:
        answer = -1
    return answer