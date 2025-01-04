n, b, w = map(int, input().split())

pebbles = input()
answer = 0
left, right = 0, 0
pebble_cnt = {'W':0, 'B':0}

pebble_cnt[pebbles[0]] += 1

while True:
    if pebble_cnt['B'] <= b and pebble_cnt['W'] >= w:
        answer = max(answer, right - left + 1)
    if pebble_cnt['B'] <= b:
        right += 1
        if right >= len(pebbles):
            break
        pebble_cnt[pebbles[right]] += 1
    else:
        pebble_cnt[pebbles[left]] -= 1
        left += 1
print(answer)