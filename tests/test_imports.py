import pytest


def test_imports():
    from project_name.lib import MyApp, MyHandler

    assert MyApp
    assert MyHandler
