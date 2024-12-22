def shuffle(cards, s, n):
    shuffled_cards = [0 for _ in range(n)]
    for i in range(n):
        shuffled_cards[s[i]] = cards[i]
    return shuffled_cards

def is_complete(cards, p, n):
    for i in range(n):
        if p[cards[i]] != i%3:
            return False
    return True

def is_initial(cards, n):
    for i in range(n):
        if i != cards[i]:
            return False
    return True

n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))

cards = [i for i in range(n)]

answer = 0
while True:
    if is_complete(cards, p, n):
        break
    answer += 1
    cards = shuffle(cards, s, n)
    if is_initial(cards, n):
        answer = -1
        break
    

print(answer)
