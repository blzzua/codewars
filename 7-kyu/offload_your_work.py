# https://www.codewars.com/kata/5b3e1dca3da310a4390000f3

def work_needed(project_minutes, free_lancers):
    remain = project_minutes - sum(f[0] * 60 + f[1] for f in free_lancers)
    if remain  > 0:
        h,m = divmod(remain, 60)
        return f'I need to work {h} hour(s) and {m} minute(s)'
    else:
        return 'Easy Money!'
    
