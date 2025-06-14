# https://www.codewars.com/kata/58fff93c31c24ad198000080

import bisect
import heapq

def processing_requests(servers, requests):
    heapq.heapify(requests)
    res = []
    for s in range(servers, 0, -1):
        ind = bisect.bisect(requests, 2*s)-1
        if ind >= 0 and requests[ind] <= 2*s:
            res.append(requests.pop(ind))
    return len(res)

# improved 
import heapq
def processing_requests(servers, requests):
    rs = requests[:]
    heapq.heapify(rs)
    res = []
    ind = len(rs)
    for s in range(servers, 0, -1):
        while rs:
            if request := rs.pop() <= 2*s:
                res.append(request)
                break
            # else: just drop last request. sorry request, this world is too cruel
    return len(res)
