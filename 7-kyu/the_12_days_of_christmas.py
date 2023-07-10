# https://www.codewars.com/kata/57dd3a06eb0537b899000a64

def sort_key(line):
    f,s,t = line.partition(' ')
    if f.isnumeric():
        return -1 * int(f)
    if f == 'a':
        return -1
    if f == 'On':
        return -13
        
def song_sorter(lines):
    return sorted(lines, key=sort_key)
