# https://www.codewars.com/kata/58e24788e24ddee28e000053

from collections import defaultdict
def simple_assembler(program):
    regs = defaultdict(int)
    p = 0
    while p < len(program):
        op, *args = program[p].split()
        if len(args) >= 1:
            r1 = args[0] 
        if len(args) == 2:
            r2 = args[1] 
        else:
            r2 = None

        match op:
            case 'mov':
                if r2.isalpha():
                    regs[r1] = regs.get(r2, 0)
                else:
                    regs[r1] = int(r2)
                p += 1
            case 'inc':
                regs[r1] += 1
                p += 1
            case 'dec':
                regs[r1] -= 1
                p += 1
            case 'jnz':
                if r1.isalpha():
                    val = regs.get(r1, 0)
                else:
                    val = int(r1)
                offset = int(r2)
                if val == 0:
                    p += 1
                else:
                    p += offset
    return regs
