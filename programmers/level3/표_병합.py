
def solution(commands):
    answer = []
    table = [[[None, -1] for _ in range(51)] for _ in range(51)]
    merge_info = {}
    global merge_cnt
    merge_cnt = 0
    
    def update1(command, merge_info):
        _,r,c,value = command
        r, c = int(r), int(c)
        if table[r][c][1] == -1:
            table[r][c][0] = value
        else:
            merge_num = table[r][c][1]
            for r,c in merge_info[merge_num]:
                table[r][c][0] = value
                
    def update2(command, merge_info):
        _, value1, value2 = command
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j][0] == value1:
                    update1(['update', i, j, value2], merge_info)
    def merge(command, merge_info):
        global merge_cnt
        _,r1,c1,r2,c2 = command
        r1,c1,r2,c2 = int(r1), int(c1), int(r2), int(c2)
        print(r1,c1,r2,c2)
        if table[r1][c1][1] == -1 and table[r2][c2][1] == -1:
            print(merge_cnt)
            print(table[r1][c1][1])
            table[r1][c1][1] = merge_cnt
        #     table[r2][c2][1] = merge_cnt
        #     merge_cnt += 1
        #     merge_info[merge_cnt] = [[r1,c1], [r2,c2]]
        # elif table[r1][c1][1] != -1 and table[r2][c2][1] == -1:
        #     merge_num = table[r1][c1][1]
        #     merge_info[merge_num].append([r2, c2])
        # elif table[r1][c1][1] == -1 and table[r2][c2][1] != -1:
        #     merge_num = table[r2][c2][1]
        #     merge_info[merge_num].append([r1, c1])
        # elif table[r1][c1][1] != -1 and table[r2][c2][1] != -1:
        #     merge_num1 = table[r1][c1][1]
        #     merge_num2 = table[r2][c2][1]
        #     for r,c in merge_info[merge_num2]:
        #         merge_info[merge_num2].append([r,c])
        #         table[r2][c2][1] = merge_num1
        #     # 터지면 merge_info 지우는 로직
        # if table[r1][c1][0] != None and table[r2][c2][0] == None:
        #     table[r2][c2][0] = table[r1][c1][0]
        #     update1(['update', r2, c2, table[r1][c1][0]], merge_info)
        # elif table[r1][c1][0] == None and table[r2][c2][0] != None:
        #     table[r1][c1][0] = table[r2][c2][0]
        #     update1(['update', r1, c1, table[r2][c2][0]], merge_info)
        # elif table[r1][c1][0] != None and table[r2][c2][0] != None:
        #     update1(['update', r2, c2, table[r1][c1][0]], merge_info)
        
    def print_t(command):
        _,r,c = command
        r, c = int(r), int(c)
        if table[r][c][0] == None:
            return 'EMPTY'
        else:
            return table[r][c][0]
        
    for command in commands:
        elem = command.split(' ')
        if elem[0] == 'UPDATE':
            if len(elem) == 4:
                update1(elem, merge_info)
            elif len(elem) == 3:
                update2(elem, merge_info)
        elif elem[0] == 'MERGE':
            merge(elem, merge_info)
        elif elem[0] == 'PRINT':
            answer.append(print_t(elem))
        
    # print(table)
    return answer

commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
solution(commands)