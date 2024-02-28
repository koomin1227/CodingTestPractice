def solution(files):
    answer = []
    file_infos = []
    
    for file in files:
        h_found, n_found = False, False
        for i in range(len(file)):
            if h_found == False and file[i].isdigit() == False and file[i + 1].isdigit():
                h = i + 1
                h_found = True
            if n_found == False and file[i].isdigit() and (i + 1 == len(file) or file[i + 1].isdigit() == False):
                n = i + 1
                n_found = True
                
        head = file[:h].lower()
        number = int(file[h:n])
        tail = ''
        if n < len(file):
            tail = file[n:].lower()
            
        file_infos.append([head, number, tail, file])
        
    file_infos.sort(key=lambda x:(x[0], x[1]))
    answer = [i[3] for i in file_infos]
    return answer