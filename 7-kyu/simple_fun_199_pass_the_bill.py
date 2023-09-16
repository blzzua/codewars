# https://www.codewars.com/kata/58c8a6daa7f31a623200016a

def pass_the_bill(total_members, conservative_party_members, reformist_party_members):
    if reformist_party_members >= (total_members+1)//2:
        return -1
    else:
        return max(0, sum(divmod((total_members+1),2)) - conservative_party_members)
