# if something in a is in b, remove all instances of it from a.
def array_diff(a, b):
    return [x for x in a if x not in b]
