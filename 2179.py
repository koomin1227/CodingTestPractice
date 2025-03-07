n = int(input())
words = []

for i in range(n):
    words.append(input())

prefix_map = {}
max_score = 0
max_prefix = ""
max_prefix_first_word_seq = ""
for i in range(len(words)):
    word = words[i]
    prefix = ""
    for char in word:
        prefix += char
        if prefix not in prefix_map:
            prefix_map[prefix] = []
        prefix_map[prefix].append(i)
        if len(prefix_map[prefix]) < 2:
            continue
        if max_score < len(prefix):
            max_score = len(prefix)
            max_prefix = prefix
            max_prefix_first_word_seq = prefix_map[prefix][0]
        elif max_score == len(prefix):
            if max_prefix_first_word_seq > prefix_map[prefix][0]:
                max_score = len(prefix)
                max_prefix = prefix
                max_prefix_first_word_seq = prefix_map[prefix][0]
            elif max_prefix_first_word_seq == prefix_map[prefix][0] and prefix_map[max_prefix][1] > prefix_map[prefix][1]:
                max_score = len(prefix)
                max_prefix = prefix
                max_prefix_first_word_seq = prefix_map[prefix][0]

for i in range(2):
    print(words[prefix_map[max_prefix][i]])
