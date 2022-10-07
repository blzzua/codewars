# https://www.codewars.com/kata/55f8ba3be8d585b81e000080

def detect_operator(num):
    # so familar.
    OPS = {'039':'Golden Telecom', '050':'MTS', '063':'Life:)', '066':'MTS', '067':'Kyivstar', '068':'Beeline', '093':'Life:)', '095':'MTS', '096':'Kyivstar', '097':'Kyivstar', '098':'Kyivstar', '099':'MTS',}
    return OPS.get(num[1:4],'no info')

