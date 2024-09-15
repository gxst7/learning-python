def intersect(t1, t2):
    """t1 and t2 are tuples
        return elements that are in both t1 and t2"""
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result


print(intersect(('t', 5, 'e'), (1, 5, 'e')))