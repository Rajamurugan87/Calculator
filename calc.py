def add(a, b):

    type1 = type(a)
    type2 = type(b)

    if type1 is not int and not float:
        raise TypeError('First Input parameter a must be a int. Instead it is ' + str(type1))

    if type2 != int and not float:
        raise TypeError('Second Input parameter a must be a int. Instead it is ' + str(type2))

    return a + b


def sub(a, b):

    type1 = type(a)
    type2 = type(b)

    if type1 is not int and not float:
        raise TypeError('First Input parameter a must be a int. Instead it is ' + str(type1))

    if type2 != int and not float:
        raise TypeError('Second Input parameter a must be a int. Instead it is ' + str(type2))

    return a - b
