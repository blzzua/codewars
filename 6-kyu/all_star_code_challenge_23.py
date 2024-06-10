# https://www.codewars.com/kata/5865dd726b56998ec4000185

def scoring(arr):
    for p in arr:
        p['scores'] = p['norm_kill'] * 100 + p['assist'] * 50 +  p['damage'] * 0.5 + p['healing'] * 1 + 2 ** p['streak'] + p['env_kill'] * 500
    return [p['name'] for p in sorted(arr, key=lambda p: p['scores'], reverse=True)]
