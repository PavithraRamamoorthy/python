import pytest


def f(x):
    raise SystemExit(5)


def test_mytest():
    with pytest.raises(SystemExit):
        f(5)