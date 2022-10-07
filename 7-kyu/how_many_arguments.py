# https://www.codewars.com/kata/5c44b0b200ce187106452139

# Create a function args_count, that returns count of passed arguments
def args_count(*args, **kwargs):
    return len(args) + len(kwargs)

