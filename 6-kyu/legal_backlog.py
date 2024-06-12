# https://www.codewars.com/kata/64c64be38f9e4603e472b53a

def legal_backlog(cases, max_daily_sessions):
    cs_time = list(cases.values())
    return max(cs_time + [int(sum(cs_time) / max_daily_sessions + 0.99)])   # int(float + 0.99) ~= math.ceil

# this kata can be solved heapq
import heapq
def legal_backlog(cases, max_daily_sessions):
    heap = []
    days = 0
    for name, v in cases.items():
        heapq.heappush(heap, -v)

    while heap:
        altered = []
        for _ in range(min(len(heap), max_daily_sessions)):
            if heap:
                altered.append(heapq.heappop(heap))
        for x in altered:
            if x!=-1:
                heapq.heappush(heap, x+1)
        days += 1
    return days
