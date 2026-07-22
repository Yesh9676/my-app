from app import greet


def test_greet():
    assert greet() == "Hello, CI/CD pipeline!"


def test_basic_math():
    assert 1 + 1 == 2
