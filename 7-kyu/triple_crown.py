# https://www.codewars.com/kata/61e173ccbc916700267ef2ae

def triple_crown(receivers):
    yards , touchdowns , receptions =  list(),list(),list()
    for r in receivers:
        yards.append(receivers[r]['Receiving yards'])
        touchdowns.append(receivers[r]['Receiving touchdowns'])
        receptions.append(receivers[r]['Receptions'])
    max_yards = max(yards)
    max_touchdowns = max(touchdowns)
    max_receptions = max(receptions)
    for r in receivers:
        #print(r, max_yards , receivers[r]['Receiving yards'] , receivers[r]['Receiving yards'] == max_yards)
        #print(r, max_touchdowns , receivers[r]['Receiving touchdowns'] , receivers[r]['Receiving touchdowns'] == max_touchdowns)
        #print(r, max_receptions , receivers[r]['Receptions'] , receivers[r]['Receptions'] == max_receptions)
        if  (receivers[r]['Receiving yards']      == max_yards      and yards.count(max_yards) == 1) \
        and (receivers[r]['Receiving touchdowns'] == max_touchdowns and touchdowns.count(max_touchdowns) == 1) \
        and (receivers[r]['Receptions']           == max_receptions and receptions.count(max_receptions) == 1):
            return r
    return 'None of them'

