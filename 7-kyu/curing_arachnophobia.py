# https://www.codewars.com/kata/5bc73331797b005d18000255

def draw_spider(leg_size, body_size, mouth, eye):
    ll = {1: '^', 2:'/\\', 3:'/╲', 4:'╱╲'}.get(leg_size,'')
    lr = {1: '^', 2:'/\\', 3:'╱\\', 4:'╱╲'}.get(leg_size,'')
    bl = '('*body_size
    br = ')'*body_size
    e = eye*(2**(body_size-1))
    return ll+bl+e+mouth+e+br+lr
