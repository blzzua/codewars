# https://www.codewars.com/kata/57547f9182655569ab0008c4

@countcalls
def replicate(times, number):
    if times > 0:
            return [number] + replicate(times-1, number) 
    else:
        return []
    

