def calc_play_time(start_time, end_time):
    return (int(end_time[:2]) * 60 + int(end_time[3:])) - (int(start_time[:2]) * 60 + int(start_time[3:]))

def convert_str_to_music(music_str):
    music = []
    for i in range(len(music_str)):
        if music_str[i] == '#':
            continue
        if i < len(music_str) - 1 and music_str[i + 1] == '#':
            music.append(music_str[i].lower())
        else:
            music.append(music_str[i])
    return music

def convert_music_to_played_music(music, play_time):
    if len(music) >= play_time:
        return music[:play_time]
    else:
        j = 0
        played_music = []
        for i in range(play_time):
            played_music.append(music[j])
            j = (j + 1) % len(music)
        return played_music


def solution(m, musicinfos):
    answer = ''
    max_play_time = 0
    remembered_music_str = ''.join(convert_str_to_music(m))
    for musicinfo in musicinfos:
        start_time, end_time, title, music_str = musicinfo.split(',')
        play_time = calc_play_time(start_time, end_time)
        music = convert_str_to_music(music_str)
        played_music = convert_music_to_played_music(music, play_time)
        played_music_str = ''.join(played_music)
        if remembered_music_str in played_music_str and max_play_time < play_time:
            answer, max_play_time = title, play_time
        
    if answer == '':
        answer = '(None)'
    return answer