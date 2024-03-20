"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    # ...
    matrix = {
        "a": "@",
        "e": "3",
        "i": "¡",
        "o": "0",
        "u": "v"
    }
    _nuevaLS = ""
    if result[0] not in matrix:
        result = result.capitalize()
    if result[-1] not in matrix:
        result = result.replace(result[-1], result[-1].upper())

    for letra in result:
        if letra in matrix:
            _nuevaLS = f"{_nuevaLS}{matrix[letra]}"
        else:
            _nuevaLS = f"{_nuevaLS}{letra}"
    result = _nuevaLS
    return result
