# https://www.codewars.com/kata/651ab89e80f7c46fc482ba12

def asteroid_collision(asteroids):
    ast = asteroids[:]
    collision_count = -1
    while collision_count != 0:
        cur_i = 0
        collision_count = 0
        while cur_i < len(ast):
            cur_ast = ast[cur_i]
            if cur_ast > 0:
                if cur_i + 1 < len(ast) and ast[cur_i + 1] < 0:
                    left, right =  ast[cur_i], ast[cur_i + 1]
                    print(left, right)
                    if abs(left) >= abs(right):
                        print('deleted', ast.pop(cur_i+1) )
                        collision_count+=1
                    if abs(left) <= abs(right):
                        print('deleted',ast.pop(cur_i) )
                        collision_count+=1
            elif cur_ast < 0:
                if cur_i - 1 >= 0 and ast[cur_i - 1] > 0:
                    left, right =  ast[cur_i-1], ast[cur_i]
                    print(left, right)
                    if abs(left) >= abs(right):
                        print('deleted',ast.pop(cur_i) )
                        collision_count+=1
                    if abs(left) <= abs(right):
                        print('deleted',ast.pop(cur_i-1) )
                        collision_count+=1
            cur_i += 1
    return ast
