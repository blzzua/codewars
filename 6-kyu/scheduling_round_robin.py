# https://www.codewars.com/kata/550cb646b9e7b565d600048a

def round_robin(jobs, time_slice, index):
    res = 0
    while jobs[index] > 0:
        for i in range(len(jobs)):
            cur_time_slice = min(jobs[i], time_slice)
            jobs[i] -= cur_time_slice
            res += cur_time_slice
            if jobs[index] == 0:
                break
    return res
