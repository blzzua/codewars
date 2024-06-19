# https://www.codewars.com/kata/57b06f90e298a7b53d000a86

def queue_time(customers, n):
    tills = [0] * n
    for i in range(n):
        if customers:
            tills[i] = customers.pop(0)
    tick = 0
    while sum(customers) + sum(tills) > 0:
        tick += 1
        for i in range(n):
            if tills[i] == 0 and len(customers) > 0:
                tills[i] = customers.pop(0)
            tills[i] = max(tills[i]-1, 0)
    return tick


# clever:
    tills = [0]*n
    for i in customers:
        tills[tills.index(min(tills))] += i
    return max(tills)

# this kata can be solved using heapq 
tills = [0] * n
for time in customers:
    heapq.heapreplace(heap, heap[0] + time)
return max(heap)
