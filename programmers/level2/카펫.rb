def solution(brown, yellow)
    answer = []
    for i in 1..yellow
        if yellow % i == 0
            c = i
            r = yellow / i
            tot = 2 * c + 2 * r + 4
            if tot == brown
                answer = [[c + 2,r + 2].max, [c + 2,r + 2].min]
                break
                
            end
        end
    end
    return answer
end