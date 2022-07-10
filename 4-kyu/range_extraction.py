# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
def solution(args):
    cur_l = [args[0],]
    ret = []
    args.append(None) # dummy
    for i in range(1,len(args)):
        if args[i] != args[i-1]+1:
            if len(cur_l) == 1:
                ret.append(str(cur_l[0]))
                cur_l.clear()
            elif len(cur_l) == 2:
                ret.append(str(cur_l[0]))
                ret.append(str(cur_l[1]))
                cur_l.clear()
            else:
                ret.append(f'{cur_l[0]}-{cur_l[-1]}')
                cur_l.clear()
        cur_l.append(args[i])
    return ','.join(ret)
