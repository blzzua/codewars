# https://www.codewars.com/kata/55c933c115a8c426ac000082

def eval_object(v):
    # python 3.10
    match v.get('operation'):
        case "+": 
            return v['a']+v['b']
        case "-": 
            return v['a']-v['b']
        case "/": 
            return v['a']/v['b']
        case "*": 
            return v['a']*v['b']
        case "%": 
            return v['a']%v['b']
        case "**": 
            return v['a']**v['b']


