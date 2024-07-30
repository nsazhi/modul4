# Глобальная область видимости
def test_function():
    def inner_function():
        print(t)

    inner_function()


t = 'Я в области видимости функции test_function'
# inner_function() --> Ошибка 'inner_function' is not defined.
test_function()