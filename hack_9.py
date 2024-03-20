"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    # ...

    result.popitem()
    for clave, valor in result.items():
        miClave = clave.capitalize()
        miValor = valor.capitalize()
        miValor = miValor.replace("k", "")
        matrix = {miClave: miValor}

    result = matrix

    return result
