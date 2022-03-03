"""
1. answer : last crew - 1 or last bus
"""
def solution(n, t, m, timetable):
    timetable = sorted([change_time_form(time) for time in timetable], reverse=True)
    current_time = change_time_form('09:00') - t

    for _ in range(n):
        num_of_person = 0
        current_time += t
       
        while num_of_person < m and len(timetable) > 0:
            if timetable[-1] <= current_time:
                num_of_person += 1
                last_passenger = timetable.pop()
            else:
                break
   
    return change_time_form(current_time) if num_of_person != m else change_time_form(last_passenger - 1)

def change_time_form(time):
    if type(time) == str:
        h, m = map(int, time.split(':'))
        return h * 60 + m
    else:
        return str(time // 60).zfill(2) + ':' + str(time % 60).zfill(2)

