# https://www.codewars.com/kata/54b724efac3d5402db00065e

#from preloaded import MORSE_CODE
MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

MORSE_CODE['|']=' ' # word separator
def decode_morse(morse_code):
    res = [MORSE_CODE.get(i,'') for i in morse_code.strip().replace('   ', ' | ').split()]
    return ''.join(res)

# best pratices
#    for morse_word in morse_code.split('   '):
#        word = ''.join(MORSE_CODE.get(morse_char, '') for morse_char in morse_word.split(' '))
#     res = ' '   .join(res)
