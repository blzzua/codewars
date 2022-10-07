# https://www.codewars.com/kata/5803956ddb07c5c74200144e

def dating_range(age):
    return f"{int(age / 2 + 7)}-{int((age - 7) * 2)}" if age > 14 else f"{int(age - 0.1 * age)}-{int(age + 0.1 * age)}"

