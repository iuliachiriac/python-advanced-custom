def my_func(x):
    if x > 0:
        return x
    else:
        return 0
    print("lala")  # code is unreachable


print(my_func(10))

result = my_func(10)
print("Result is:", result)
print("Result incremented:", result + 1)
print("call other function on result:", pow(result, 2))


def my_func_print(x):
    if x > 0:
        print(x)
    else:
        print(0)
    print("lala")  # code is reachable


result = my_func_print(10)
print("Result is:", result)


# Return early pattern
def get_longer_strings(*args: str, min_length=None):
    if not min_length:
        return list(args)
    # code below is executed only if condition above is False
    strings = []
    for string in args:
        if len(string) > min_length:
            strings.append(string)
    return strings
