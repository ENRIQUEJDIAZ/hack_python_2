"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    # ...
    nuevo = []
    num = 0
    # ...
    if len(result) == 0:
        nuevo = ["0"]
    else:
        for paso in result:
            num += 1
            if num % 2 == 0:
                valor = "-"
            else:
                valor = num
            nuevo.append(f"{valor}")
    result = nuevo
    return result
