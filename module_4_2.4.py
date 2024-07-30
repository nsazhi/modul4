# Встроенная область видимости

from module_4_2_2 import t


def test_function():
    def inner_function():
        print(t)

    inner_function()


# inner_function() --> Ошибка 'inner_function' is not defined.
test_function()
