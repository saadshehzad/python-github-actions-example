from app import index


def test_index():
    return index() == "Hello World"