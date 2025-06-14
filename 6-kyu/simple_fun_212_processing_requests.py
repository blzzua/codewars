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
