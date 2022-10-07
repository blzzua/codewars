# https://www.codewars.com/kata/5b609ebc8f47bd595e000627

def solution(arr_val, arr_unit):
    print(arr_unit)
    G = 6.67*(10**-11)
    kg = {"g" : 0.001, "mg" : 1 * (10**-6), "μg" : 1 * (10**-9), "lb" : 0.453592}
    meter = {'cm': 0.01, "mm" : 0.001, "μm" : 1 * (10**-6), "ft" : 0.3048 }
    m1 = kg.get(arr_unit[0],1.0) * float(arr_val[0])
    m2 = kg.get(arr_unit[1],1.0) * float(arr_val[1])
    d = meter.get(arr_unit[2],1.0) * float(arr_val[2])
    f = (G * m1 * m2) / (d**2)
    return f


