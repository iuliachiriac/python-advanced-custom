# Intentionally problematic Python code to trigger PyCharm inspections


def calculate(value):
    """
    This is a docstring
    :param value:
    :return:
    """
    result = value * 2
    return result


def unused_function():
    pass


class TestClass:
    def __init__(self, value):
        self.value = value

    def method_name(self):
        print(f"Hello, world! I am {self}")


if __name__ == "__main__":
    print(calculate(10))

    for i in range(5):
        print(i)

    if True:
        print("Missing colon")
