# https://www.codewars.com/kata/5a53a17bfd56cb9c14000003

def disarium_number(number):
    return ['Not !!', 'Disarium !!'][sum( int(n)**i for i,n in enumerate(str(number),1)) == number]


