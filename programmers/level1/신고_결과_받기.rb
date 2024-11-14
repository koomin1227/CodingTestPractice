def solution(id_list, report, k)
    answer = []
    reported_list = {}
    mail_list = {}
    
    id_list.each{ |id|
        reported_list[id] = []
        mail_list[id] = 0
    }
    
    report.each{ |re|
        reporter, user = re.split " "
        if !reported_list[user].include?(reporter)
            reported_list[user] << reporter
        end
    }
    
    id_list.each{ |id|
        if reported_list[id].length >= k
            reported_list[id].each{ |mail_id|
                mail_list[mail_id] += 1
            }
        end
    }
    
    id_list.each{ |key|
        answer << mail_list[key]
    }

    return answer
end