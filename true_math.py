def divide(first, second):
    from math import inf
    if first == 0 or second == 0:
        return inf
    else:
        div_ = first/second
        return div_

if __name__ == '__mane__':
    divide()