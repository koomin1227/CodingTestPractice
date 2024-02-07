def solution(today, terms, privacies):
    answer = []
    nterms = {}
    def date_to_int(date):
        day = []
        for i in date.split('.'):
            day.append(int(i))
        return day[0] * 12 * 28 + day[1] * 28 + day[2]
    for term in terms:
        kind, period = term.split(' ')
        nterms[kind] = 28 * int(period)
    
    today_day = date_to_int(today)
    for i in range(len(privacies)):
        privacy = privacies[i]
        start_date, term = privacy.split(' ')
        if date_to_int(start_date) + nterms[term] <= today_day:
            answer.append(i + 1)
    return answer