# https://www.codewars.com/kata/57f8842367c96a89dc00018e

def cat_mouse(map_, moves):
    cols = map_.index('\n') 
    rows = map_.count('\n') + 1
    mmap = map_.replace('\n','')
    m = mmap.find('m')
    c = mmap.find('C')
    if -1 in (m, c):
        return 'boring without two animals'
    md = divmod(m , cols)
    cd = divmod(c , cols)
    if sum(abs(a-b) for a,b in zip(md, cd)) <= moves:
        return 'Caught!'
    else:
        return 'Escaped!'
