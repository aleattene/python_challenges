"""
Python solution for challenge: "Hello, Name or World!"
To start the tests, type from CLI: python tests-.py
"""


def hello(name=""):
    return f'Hello, {name.capitalize()}!' if name else "Hello, World!"
