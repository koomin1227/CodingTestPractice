from collections import defaultdict
import math

def make_set(str_list):
    str_set = []
    for i in range(len(str_list) - 1):
        tmp = ''.join(str_list[i:i+2])
        if tmp.isalpha():
            str_set.append(tmp)
    return str_set

def find_intersect(str1, str2):
    res = []
    inter_set = set(str1.keys()) & set(str2.keys())
    for i in inter_set:
        res += [i] * min(str1[i], str2[i])
    return len(res)

def find_union(str1, str2):
    res = []
    union_set = set(str1.keys()) | set(str2.keys())
    for i in union_set:
        res += [i] * max(str1[i], str2[i])
    return len(res)

def solution(str1, str2):
    answer = 0
    str1_set_list, str2_set_list = make_set(str1.lower()), make_set(str2.lower())
    str1_dict, str2_dict = defaultdict(int), defaultdict(int)
    
    for c in str1_set_list:
        str1_dict[c] += 1
    for c in str2_set_list:
        str2_dict[c] += 1
        
    intersect_cnt = find_intersect(str1_dict, str2_dict)
    union_cnt = find_union(str1_dict, str2_dict)
    if intersect_cnt == 0 and union_cnt == 0:
        return 65536
    answer = math.floor((intersect_cnt / union_cnt) * 65536)
    return answer