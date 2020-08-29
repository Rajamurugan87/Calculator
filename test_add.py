import pytest

from calc import add

#Annotation


@pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),
        (1000000, 2000000, 3000000),
        ('1', '2', '3'),
        (None, None, None),
        (1.4, 4, 5.4),
        (2+3j, 4+5j, 6+8j)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# DRY - DO NOT REPEAT YOURSELF


# def test_add_characters():
#     return_value = add('1', '2')
#     print(type(return_value))
#     assert return_value == 3


# def test_add_float():
#     return_value = add(1.4, 4)
#     print(type(return_value))
#     assert return_value == 5.4


# def test_add_complex():
#     return_value = add(2+3j, 4+5j)
#     print(type(return_value))
#     assert return_value == 6 + 8j


# def test_sub_elementary():
#     assert subst(3, 2) == 1
#
#
# def test_sub_high_school():
#     assert subst(2000000, 1000000) == 1000000
#
#
# def test_sub_characters():
#     return_value = subst('1', '2')
#     print(type(return_value))
#     assert return_value == 3
#
#
# def test_sub_float():
#     return_value = subst(1.4, 4)
#     print(type(return_value))
#     assert return_value == 5.4
#
#
# def test_sub_complex():
#     return_value = subst(2+3j, 4+5j)
#     print(type(return_value))
#     assert return_value == 6 + 8j
