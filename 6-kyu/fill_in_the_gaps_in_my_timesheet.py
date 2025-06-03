# https://www.codewars.com/kata/564871e795df155582000013

def fill_gaps(timesheet):
    if len(timesheet) < 3:
        return timesheet
    res = []
    prev = timesheet[0]
    for cur in timesheet:
        res.append(cur)
        if cur is not None:
            if prev == cur:
                i = len(res) - 2
                while res[i] is None:
                    res[i] = prev
                    i = i - 1
            else:
                prev = cur
    return res
