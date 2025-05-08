# https://www.codewars.com/kata/5886f3713a111b620f0000dc

def html_end_tag_by_start_tag(start_tag):
    return ('</' + start_tag.partition(' ')[0][1:] + '>').replace('>>','>')
