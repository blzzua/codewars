# https://www.codewars.com/kata/6638277786032a014d3e0072

def allocate_rooms(customers):
    cust_list = []
    for i, customer in enumerate(customers):
        cust_list.append({'arrival': customer[0], 'departure': customer[1], 'num': i, 'room': 0 })
    cust_list.sort(key=lambda x: x['arrival'])

    rooms = []
    for customer in cust_list:
        free_room_index = -1
        for i, room_end_day in enumerate(rooms):
            if customer['arrival'] > room_end_day:
                free_room_index = i
                break
        if free_room_index < 0:
            rooms.append(customer['departure'])
            customer['room'] = len(rooms)
        else:
            rooms[free_room_index] = customer['departure']
            customer['room'] = free_room_index + 1
    res = []
    for customer in sorted(cust_list, key=lambda c: c['num']):
        res.append(customer['room'])
    return res
