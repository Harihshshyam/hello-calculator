import pytest
from app import add, sub

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2

@pytest.mark.parametrize("op,a,b,expect", [
    ('add', 1, 2, 3),
    ('sub', 5, 2, 3),
])
def test_parametrized(op, a, b, expect):
    if op == 'add':
        assert add(a, b) == expect
    else:
        assert sub(a, b) == expect

