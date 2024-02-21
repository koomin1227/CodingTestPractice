def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return 5 * len(cities)
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
    return answer