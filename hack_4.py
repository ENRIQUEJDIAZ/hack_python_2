"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    # ...
    cant = len(result)
    if cant > 3:
        result = result.replace(result[0], "")
        result = result.replace(result[-1], "")
    return result
