# https://www.codewars.com/kata/535a69fb36973f2aad000953

def shortener(message):
    while True:
        if len(message) <= 160:
            return message
        if ' ' not in message:
            break
        words = message.split()
        last, prev = words.pop(), words.pop()
        tail = prev + last[0].upper() + last[1:]
        message = ' '.join(words + [tail])
    return message
  
