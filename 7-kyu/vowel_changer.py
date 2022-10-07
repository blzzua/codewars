# https://www.codewars.com/kata/597754ba62f8a19c98000030

def vowel_change(txt, vow):
    return ''.join(vow if c in 'aeiou' else c for c in txt)

