"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    # ...
    nuevo = []
    num = 0
    if len(result) == 1:
        nuevo = [0]
    else:
        for paso in result:
            num += 1
            if num % 2 == 0:
                nuevo.append(num)
            else:
                nuevo.append(f"{num}")
    result = nuevo
    return result
