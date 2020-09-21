# -*- coding: utf-8 -*-

import pytest
from dyno.skeleton import fib

__author__ = "Sean Koval"
__copyright__ = "Sean Koval"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
