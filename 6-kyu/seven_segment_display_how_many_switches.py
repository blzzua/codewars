# https://www.codewars.com/kata/64a6e4dbb2bc0500171d451b

ind_map = {' ': '0000000', '0': '1111110', '1': '0110000', '2': '1101101', '3': '1111001', '4': '0110011', '5': '1011011', '6': '1011111', '7': '1110000', '8': '1111111', '9': '1111011'}

def count_segment_switches(display_size: int, sequence: list[int]) -> int:
    sequence = [' '* display_size] + [str(digit).rjust(display_size) for digit in sequence]
    cnt = 0
    for number1, number2 in zip(sequence,  sequence[1:]):
        for d1,d2 in zip(number1, number2):
            for bit1, bit2 in zip(ind_map[d1], ind_map[d2]):
                if bit1 != bit2:
                    cnt += 1
    return cnt
  
