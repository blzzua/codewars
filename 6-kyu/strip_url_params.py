# https://www.codewars.com/kata/51646de80fd67f442c000013

def strip_url_params(url, params_to_strip=[]):
    if '?' not in url:
        return url

    param_dict = {}
    host, qsep, params = url.partition('?')
    for param_str in params.split('&'):
        param, _, value = param_str.partition('=')  
        if param not in param_dict:
            param_dict[param] = value
    for k in params_to_strip:
        if k in param_dict:
            del param_dict[k]

    if param_dict:
        return host + qsep + '&'.join([f'{k}={v}' for k, v in param_dict.items()])
    else:
        return host
