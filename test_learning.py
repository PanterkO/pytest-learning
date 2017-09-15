'''
pytest --fixtures - показывает все созданные фикстуры в проекте

'''

import pytest

def func(x):
    return x+1

def test_answer():
    assert func(3) == 4

def f():
    raise SystemExit(1)

def test_f():
    with pytest.raises(SystemExit):
        f()

class TestClass(object):
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'

        assert hasattr(x, 'hello')

def test_needfiles(tmpdir):
    print(tmpdir)
    assert 0
