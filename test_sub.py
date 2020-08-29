import pytest

from calc import sub


@pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),
        (1000000, 2000000, 3000000),
        ('1', '2', '3'),
        (None, None, None),
        (1.4, 4, 5.4),
        (2+3j, 4+5j, 6+8j)
])
def test_sub(a, b, expected):
    assert sub(a, b) == expected
