import pytest

from string_utils import StringUtils


utils = StringUtils()


@pytest.mark.parametrize("value, expected", [
    ("skypro", "Skypro"),
    ("тест", "Тест"),
    ("hello world", "Hello world"),
    ("123abc", "123abc"),
    ("", ""),
    (" ", " "),
    ("  skypro", "  skypro"),
])
def test_capitalize(value, expected):
    assert utils.capitalize(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("   skypro", "skypro"),
    (" sky pro ", "sky pro "),
    ("skypro", "skypro"),
    ("", ""),
    (" ", ""),
    ("   ", ""),
    ("  123", "123"),
])
def test_trim(value, expected):
    assert utils.trim(value) == expected


@pytest.mark.parametrize("value, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("Тест", "е", True),
    ("123", "2", True),
    ("04 апреля 2023", "апреля", True),
    ("", "x", False),
    (" ", "x", False),
    ("SkyPro", "sky", False),
])
def test_contains(value, symbol, expected):
    assert utils.contains(value, symbol) is expected


@pytest.mark.parametrize("value, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("banana", "a", "bnn"),
    ("test", "z", "test"),
    ("", "x", ""),
    (" ", " ", ""),
    ("04 апреля 2023", " ", "04апреля2023"),
    ("aaa", "aa", "a"),
])
def test_delete_symbol(value, symbol, expected):
    assert utils.delete_symbol(value, symbol) == expected


@pytest.mark.parametrize("method, args", [
    ("capitalize", (None,)),
    ("trim", (None,)),
    ("contains", (None, "a")),
    ("delete_symbol", (None, "a")),
])
def test_invalid_none_raises_type_error(method, args):
    with pytest.raises((TypeError, AttributeError)):
        getattr(utils, method)(*args)
