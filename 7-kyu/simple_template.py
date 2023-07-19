# https://www.codewars.com/kata/56ae72854d005c7447000023

import re

def create_template(template):
    def response(**kwargs):
        response_text = template
        for k,v in kwargs.items():
             response_text = response_text.replace('{{'+k+'}}',v)
        response_text = re.sub(r'{{\w+}}','',response_text)
        return response_text
    return response

