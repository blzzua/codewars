# https://www.codewars.com/kata/52b7ed099cdc285c300001cd
  
def sum_of_intervals(intervals):
    sorted_intervals = sorted(intervals)
    prev = list(sorted_intervals[0])
    accumulated = []
    for cur in sorted_intervals[1:]:
        # print('processing', cur, 'with', prev)
        if prev[1] > cur[1]:
            # print('skip', prev)
            continue
        elif cur[0] < prev[1] and prev[1] < cur[1]:
            # print('expanding prev:', prev, 'to', prev[0], cur[1] )
            prev[1] = cur[1]
        elif prev[1] == cur[0]:
            # print('concatenate prev:', prev)
            prev[1] = cur[1]
        if cur[0] > prev[1]:
            # print('added', prev)
            accumulated.append(tuple(prev))
            prev = list(cur[:])
    accumulated.append(tuple(prev))
    return sum( b-a for a,b in accumulated)
    
