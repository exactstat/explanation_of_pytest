import pytest
from code_for_test import *

# название файла с тестами должно начинаться изи заканчиваться на test_, _test
# название функции с тестами должно начинаться изи заканчиваться на test_, _test
# From cmd run: py.test -v -s

@pytest.fixture() # Этот декоратор обозначает что эта функция будет использована как фикстура
def before_every_method():
    print("\nThis method runs before every method in test.")


def test_app(before_every_method):
    print("\nRunning app\n")
    my_app(1, 2)

