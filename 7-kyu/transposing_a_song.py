# https://www.codewars.com/kata/55b6a3a3c776ce185c000021

def transpose(song, interval):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    notes = notes + notes
    d = {"Bb": "A#", "Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#"}
    return [notes[(notes.index(d.get(i, i)) + interval)] for i in song]

