# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

def validate_battlefield(field):
    #very ugly solution. but i have to beat this kata
    n_max = len(field) - 1
    n_min = 0
    for y_n, y_row in enumerate(field):
        for x_n, val in enumerate(y_row):
            if val == 1:
                v_pos_r = field[y_n+1][x_n] if y_n+1 <= n_max else 0
                v_pos_l = field[y_n-1][x_n] if n_min <= y_n-1 else 0
                h_pos_r = field[y_n][x_n+1] if x_n+1 <= n_max else 0
                h_pos_l = field[y_n][x_n-1] if n_min <= x_n-1 else 0
                if v_pos_l + v_pos_r > 0 and h_pos_r + h_pos_r > 0:
                    #print ('overlap')
                    return False
            if val == 1 and n_min < y_n < n_max and  n_min < x_n < n_max:
                d_pos_1 = field[y_n-1][x_n-1] if (n_min <= y_n-1) or (n_min <= x_n-1)  else 0
                d_pos_2 = field[y_n-1][x_n+1] if (n_min <= y_n-1) or (x_n+1 <= n_max) else 0
                d_pos_3 = field[y_n+1][x_n+1] if (y_n+1 <= n_max) or (x_n+1 <= n_max) else 0
                d_pos_4 = field[y_n+1][x_n-1] if (y_n+1 <= n_max) or (n_min <= x_n-1) else 0
                if d_pos_1 + d_pos_2 + d_pos_3 + d_pos_4 > 0 :
                    #print ('diag overlap at {x_n}x{y_n} in {d_pos_1}+{d_pos_2}+{d_pos_3}+{d_pos_4}')
                    return False

                
    #print ('phaze 2 count and remove submarines')
    l1 = 0
    new_field=[] 
    for y_n, y_row in enumerate(field):
        new_field.append(y_row[:])
        for x_n, val in enumerate(y_row):
            if val == 1:
                v_pos_r = field[y_n+1][x_n] if y_n+1 <= n_max else 0
                v_pos_l = field[y_n-1][x_n] if n_min <= y_n-1 else 0
                h_pos_r = field[y_n][x_n+1] if x_n+1 <= n_max else 0
                h_pos_l = field[y_n][x_n-1] if n_min <= x_n-1 else 0
                if (v_pos_r, v_pos_l, h_pos_r, h_pos_l) == (0, 0, 0, 0):
                    l1 = l1 + 1
                    new_field[y_n][x_n] = 0
    if l1 != 4:
        #print ('sumbarines != 4')
        return False

    #print ('phaze 3 count other horisontal boats')
    c2 , c3 , c4 , prev = 0, 0, 0, 0
    for linenum,l0 in enumerate(field):
        i=0
        prev=0
        l = l0[:]
        l.append(0)
        while i < len(l):
            if prev == 0:
                if l[i] > 0:
                    prev = prev + 1
            else:
                if l[i] > 0 :
                    prev = prev +1
                elif l[i] == 0 :
                    if prev == 2:
                        #print(f'found 2-b at {linenum}x{i} : {l} ')
                        c2 += 1
                    if prev == 3:
                        #print(f'found 3-b at {linenum}x{i} : {l} ')
                        c3 += 1
                    if prev == 4:
                        #print(f'found 4-b at {linenum}x{i} : {l} ')
                        c4 += 1
                    prev = 0
            i = i + 1

            new_field=[]
    
    #print ('phase 4 transpose')
    for y_n, y_row in enumerate(field):
        new_field.append(y_row[:])
        for x_n, val in enumerate(y_row):
            new_field[y_n][x_n] = field[x_n][y_n]
    
    #print ('phase 5 count vertical boats same as horisontal but on transposed field')
    prev = 0 
    for linenum,l0 in enumerate(new_field):
        i=0
        prev=0
        l = l0[:]
        l.append(0)
        while i < len(l):
            if prev == 0:
                if l[i] > 0:
                    prev = prev + 1
            else:
                if l[i] > 0 :
                    prev = prev +1
                elif l[i] == 0 :
                    if prev == 2:
                        #print(f'found 2-b at {linenum}x{i} : {l} ')
                        c2 += 1
                    if prev == 3:
                        #print(f'found 3-b at {linenum}x{i} : {l} ')
                        c3 += 1
                    if prev == 4:
                        #print(f'found 4-b at {linenum}x{i} : {l} ')
                        c4 += 1
                    prev = 0
            i = i + 1
    if (c2,c3,c4) != (3,2,1):
        return False
    return True
