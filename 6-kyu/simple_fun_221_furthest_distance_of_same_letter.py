# https://www.codewars.com/kata/5902bc48378a926538000044

def dist_same_letter(st):
    seen_letters = set()
    res = {}
    for i, letter in enumerate(st):
        if letter not in seen_letters:
            last_ind = st.rfind(letter)
            res[letter] = last_ind - i + 1
            seen_letters.add(letter)
    letter, index = max(res.items(), key=lambda kv: kv[1])
    return f'{letter}{index}'
