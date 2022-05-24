"""
1. Handle string
2. regex
"""

import re

def solution(m, musicinfos):
    answer_list = []
    m = '.'.join(re.findall(r'[CDEFGAB]#*', m)) + '.'
       
    for musicinfo in musicinfos:
        start_time, end_time, title, scales = musicinfo.split(',')
        total_minutes = get_total_minutes(start_time, end_time)
        scales = re.findall(r'[CDEFGAB]#*', scales)
        scales = (total_minutes // len(scales)) * scales + scales[:total_minutes % len(scales)]
        scales = '.'.join(scales) + '.'

        if m in scales:
            answer_list.append((title, total_minutes, start_time))

    answer_list.sort(key=lambda x : (-x[1], x[2]))
   
    return "(None)" if len(answer_list) == 0 else answer_list[0][0]


def get_total_minutes(start_time, end_time):
    """
    input : start_time, end_time ("HH:MM")
    output : minutes (int)
    """
    e_hour, e_minute = map(int, end_time.split(':'))
    s_hour, s_minute = map(int, start_time.split(':'))

    return (e_hour - s_hour) * 60 + e_minute - s_minute
