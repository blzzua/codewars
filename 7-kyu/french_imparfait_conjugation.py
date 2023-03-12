# https://www.codewars.com/kata/6394c1995e54bd00307cf768

def to_imparfait(verb_phrase):
    noun = verb_phrase.split()[0]
    ending_map = {'Je': 'ais', 'Tu': 'ais', 'Il': 'ait', 'Elle': 'ait', 'On': 'ait', 'Nous': 'ions', 'Vous': 'iez', 'Ils': 'aient', 'Elles': 'aient'}
    return verb_phrase[:-2] + ending_map[noun]
