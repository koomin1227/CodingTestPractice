from collections import deque
s = int(input())

que = deque()
que.append((1, 0, -1))
is_visited = [[False] * 1001 for _ in range(1001)]
is_visited[1][0] = True
while que:
    emoji_cnt, time, clipboard = que.popleft()
    if emoji_cnt == s:
        print(time)
        break
    for i in range(3):
        if i == 0:
            new_emoji_cnt, new_clipboard = emoji_cnt - 1, clipboard
        elif i == 1:
            new_emoji_cnt, new_clipboard = emoji_cnt, emoji_cnt
        else:
            new_emoji_cnt, new_clipboard = emoji_cnt + clipboard, clipboard

        if new_emoji_cnt >= 1001 or new_emoji_cnt < 0 or new_clipboard >= 1001 or new_clipboard < 0 or is_visited[new_emoji_cnt][new_clipboard]:
            continue


        is_visited[new_emoji_cnt][new_clipboard] = True
        que.append((new_emoji_cnt, time + 1, new_clipboard))

