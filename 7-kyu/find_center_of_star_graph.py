# https://www.codewars.com/kata/63b9aa69114b4316d0974d2c

def center(graph_edges):
    return set(graph_edges[0]).intersection(set(graph_edges[1])).pop()
