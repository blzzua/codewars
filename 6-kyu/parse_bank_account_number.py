# https://www.codewars.com/kata/597eeb0136f4ae84f9000001

digits_str = """
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
""".strip('\n')
triades = list(zip(*digits_str.split('\n')))
digit_map = {code_tuple: value  for value, code_tuple in enumerate(zip(triades[0::3], triades[1::3], triades[2::3]))}

def parse_bank_account(bank_account):
    bank_account = bank_account.strip('\n')
    cols = list(zip(*bank_account.split('\n')))
    return int(''.join([str(digit_map.get(code_tuple,0))  for code_tuple in zip(cols[0::3], cols[1::3], cols[2::3])]))
