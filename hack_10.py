"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    # ...
    indice = 0
    valor = 0
    vector = []
    # ...
    for pasos in result:
        print(pasos)
        indice = valor + 1
        valor = indice + 1
        vector.append({f"{indice}": f"{valor}"})
    result = vector
    return result
