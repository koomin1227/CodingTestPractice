def solution(players, callings)
    answer = []
    p_rank = {}
    r_player = {}
    
    for i in 0..players.length - 1
        p_rank[players[i]] = i
        r_player[i] = players[i]
    end
    
    callings.each { |calling|
        rank = p_rank[calling]
        next_player = r_player[rank - 1]
        p_rank[calling] = rank - 1
        p_rank[next_player] = rank
        r_player[rank] = next_player
        r_player[rank - 1] = calling
    }
    
    r_player.keys.each { |key|
        answer << r_player[key]
    }

    return answer
end