def solution(name, yearning, photo)
    answer = []
    score = Hash.new(0)
    for i in 0..name.length - 1
        score[name[i]] = yearning[i]
    end

    for i in 0..photo.length - 1
        tot = 0
        photo[i].each { |n|
            tot = tot + score[n]
        }
        answer << tot
    end
    return answer
end