"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    # ...
    cant = len(result)
    # ...
    if cant % 2 == 0:
        for indice in range(cant):
            result[indice] = f"{indice+1}"
    else:
        for indice in range(cant):
            result[indice] = f"{result[indice]}{'-'}{indice+1}"

    result.reverse()
    return result
