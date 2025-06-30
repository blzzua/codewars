# https://www.codewars.com/kata/58957c5041c979cf9e00002f

def boxes_packing(length, width, height):
    boxes = sorted([sorted([l, w, h], reverse=True) for l, w, h in zip(length, width, height)], reverse=True)
    for b1, b2 in zip(boxes, boxes[1:]):
        if b1[0] <= b2[0]:
            print(f'{b2} not fit in {b1} in 0-dimenstion')
            return False
        if b1[1] <= b2[1]:
            print(f'{b2} not fit in {b1} in 1-dimenstion')
            return False
        if b1[2] <= b2[2]:
            print(f'{b2} not fit in {b1} in 2-dimenstion')
            return False
    return True
