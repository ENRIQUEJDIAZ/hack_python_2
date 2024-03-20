"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    _lista = []
    _palabra = []
    # ...
    cantidad = len(result)
    primer_letra = result[0]
    if primer_letra != "f":
        for i in range(0, cantidad, 3):
            _lista.append(result[i:i+3])

        for silabas in _lista:
            if len(silabas) % 2 != 0:
                contenedor = f"{silabas[0:2]}{'-'}"
                _palabra.append(contenedor)
            else:
                _palabra.append(silabas)
    else:
        for i in range(0, cantidad):
            _lista.append(result[i])
        _lista[2] = "-"
        _lista[7] = "-"
        _lista.insert(5, "-")
        for silabas in _lista:
            _palabra.append(silabas)
    result = "".join(_palabra)
    return result
