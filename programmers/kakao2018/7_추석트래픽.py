"""
1. Handle string
2. Queue
"""
from collections import deque

def solution(lines):
    answer = 0
    traffic_start_times, traffic_end_times = [], []
   
    for line in lines: # line format : "YYYY-MM-DD HH:MM:SS.SSS S.Ss"
        time_form = line[:-1].split()
        h, m, s = map(float, time_form[1].split(':'))
        end_time = h*3600 + m*60 + s
        start_time = round(end_time - float(time_form[2]) + 0.001, 4)
        traffic_start_times.append(start_time)
        traffic_end_times.append(end_time)
   
    traffic_start_times.sort()
    traffic_end_times = deque(sorted(traffic_end_times))
   
    current_count = 0
    for traffic_start_time in traffic_start_times:
        current_count += 1
        time_bound = round(traffic_start_time - 0.999, 4)
       
        while traffic_end_times[0] < time_bound:
            traffic_end_times.popleft()
            current_count -= 1
           
        answer = max(answer, current_count)
   
    return answer

